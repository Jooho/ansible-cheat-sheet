#!/usr/bin/env python

from __future__ import print_function
from collections import defaultdict
from xml.dom import minidom

import libvirt
import argparse
import os
import sys
import subprocess

try:
    import ConfigParser as configparser
except ImportError:
    import configparser

try:
    import json
except ImportError:
    import simplejson as json


def parse_args():
    """
    Create command line parser for libvirt dynamic inventory script.
    """
    parser = argparse.ArgumentParser(
        description='Ansible dynamic inventory script for Libvirt.',
    )
    parser.add_argument(
        '--list',
        action='store_true',
        default=True,
        help='Get data of all virtual machines (default: True).',
    )
    parser.add_argument(
        '--host',
        help='Get data of virtual machines running on specified host.',
    )
    parser.add_argument(
        '--pretty',
        action='store_true',
        default=False,
        help='Pretty format (default: False).',
    )
    return parser.parse_args()

def load_config_file():
    # Get the path of the configuration file, by default use
    # 'libvirt.ini' file in script directory:
    default_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'libvirt.ini',
    )
    config_path = os.environ.get('LIBVIRT_INI_PATH', default_path)

    # Create parser and add ovirt section if it doesn't exist:
    config = configparser.SafeConfigParser(
        defaults={
            'libvirt_connection_url': None
        }
    )
    if not config.has_section('libvirt'):
        config.add_section('libvirt')
    config.read(config_path)

    return config


def create_connection():
    """
    Create a connection to libvirt engine API.
    """

    config = load_config_file()

    # Create a connection with options defined in ini file:
    url = config.get('libvirt', 'libvirt_connection_url')
    conn = libvirt.open(url)

    if conn == None:
      print("Failed to open connection to %s" % (url), file=sys.stderr)
      exit(1)
    return conn


def get_dict_of_struct(connection, target_vm_name):

    data={}
    vm = connection.lookupByName(target_vm_name)

    # VM state
    state, reason = vm.state()
    if state == libvirt.VIR_DOMAIN_NOSTATE:
        _state = 'NOSTATE'
    elif state == libvirt.VIR_DOMAIN_RUNNING:
        _state = 'RUNNING'
    elif state == libvirt.VIR_DOMAIN_BLOCKED:
        _state = 'BLOCKED'
    elif state == libvirt.VIR_DOMAIN_PAUSED:
        _state = 'PAUSED'
    elif state == libvirt.VIR_DOMAIN_SHUTDOWN:
        _state = 'SHUTDOWN'
    elif state == libvirt.VIR_DOMAIN_SHUTOFF:
        _state = 'SHUTOFF'
    elif state == libvirt.VIR_DOMAIN_CRASHED:
        _state = 'CRASHED'
    elif state == libvirt.VIR_DOMAIN_PMSUSPENDED:
        _state = 'PMSUSPENDED'
    else:
        _state = 'UNKNOWN'


    if _state == 'RUNNING':
        # VM Network interface
        ifaces = vm.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)
        vm_ip=''
        for (name, val) in ifaces.iteritems():
            if val['addrs']:
                for ipaddr in val['addrs']:
                    if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4 and ipaddr['addr'] != '127.0.0.1':
                        vm_ip = ipaddr['addr']

        # Hostname
        cmd = subprocess.Popen("host vm_ip", shell=True, stdout=subprocess.PIPE)
        #cmd = subprocess.Popen("host 1.8.8.8", shell=True, stdout=subprocess.PIPE)
        vm_hostname=''

        for line in cmd.stdout:
            if "pointer" in line:
                hostnm = line.rsplit(' ',1)[1]
                vm_hostname = hostnm[:-2]
            else:
                vm_hostname = 'NXDOMAIN'

        data={
             'name': vm.name(),
             'status': _state,
             'os_type': vm.OSType(),
             'memory': str(vm.info()[2]),
             'max_memory': str(vm.maxMemory()),
             'cpu': str(vm.info()[3]),
             'max_cpu': str(vm.maxVcpus()),
             'ip': vm_ip,
             'hostname': vm_hostname
         }
    else:
        data={
            'name': vm.name(),
            'status': _state,
            'memory': str(vm.info()[2]),
            'max_memory': str(vm.maxMemory()),
            'cpu': str(vm.info()[3]),
         }

    return data



def get_data(connection, target_vm_name=None):
    """
    Obtain data of `target_vm_name` if specified, otherwise obtain data of all vms.
    """
    all_vms_name_list = connection.listAllDomains()
    active_vms_id_list = connection.listDomainsID()
    active_vms_name_list = []
    
    # VM ID ==> VM Name
    if len(active_vms_id_list) != 0:
        for vmID in active_vms_id_list:
            vm = connection.lookupByID(vmID)
            active_vms_name_list.append(vm.name())

    # Check if target VM is running
    # if it is running, return only the VM data. If not, return all VM data.
    if target_vm_name and target_vm_name in active_vms_name_list:
        data = get_dict_of_struct(
            connection=connection,
            target_vm_name=target_vm_name,
        )
    else:
        vms = dict()
        data = defaultdict(list)
        for vm in all_vms_name_list:
            name = vm.name()

            # Add vm to vms dict
            vms[name] = get_dict_of_struct(connection, name)

            # Add vm to group by OKD version (Additional Data for OKD)
            okd_version = vm.name().split('_')[0]

            if okd_version in vm.name():
                data['group_%s_all' % okd_version].append(vm.name())
                if 'master' in vm.name():
                    data['group_%s_masters' % okd_version].append(vm.name())
                if 'app_node' in vm.name():
                    data['group_%s_app_nodes' % okd_version].append(vm.name())
                if 'infra_node' in vm.name():
                    data['group_%s_infra_nodes' % okd_version].append(vm.name())
                if 'etcd' in vm.name():
                    data['group_%s_etcd_nodes' % okd_version].append(vm.name())
                if 'lb' in vm.name():
                    data['group_%s_lb_nodes' % okd_version].append(vm.name())

        data["_meta"] = {
            'hostvars': vms,
        }

    return data


def main():
    args = parse_args()
    connection = create_connection()

    print(
        json.dumps(
            obj=get_data(
                connection=connection,
                target_vm_name=args.host,
            ),
            sort_keys=args.pretty,
            indent=args.pretty * 2,
        )
    )

if __name__ == '__main__':
    main()
