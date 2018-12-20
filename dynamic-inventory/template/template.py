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
   
    ### UPDATE for config file name ###
    default_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'libvirt.ini',     # <=========
    )
    #######################

    config_path = os.environ.get('LIBVIRT_INI_PATH', default_path)

    # Create parser and add ovirt section if it doesn't exist:
    config = configparser.SafeConfigParser(
     ### UPDATE for default values ###
        defaults={
            'libvirt_connection_url': None    # <=========
        }
    )
    if not config.has_section('libvirt'):
        config.add_section('libvirt')       # <========
    #########################

    config.read(config_path)

    return config


def create_connection():
    """
    Create a connection to libvirt engine API.
    """

    config = load_config_file()

    # Create a connection with options defined in ini file:
    ### UPDATE for connection ####
    url = config.get('libvirt', 'libvirt_connection_url')
    conn = libvirt.open(url)
    ###############
    if conn == None:
      print("Failed to open connection to %s" % (url), file=sys.stderr)
      exit(1)
    return conn


def get_dict_of_struct(connection, target_vm_name):

    data={}

    ### UPDATE ###

    ###################
    return data



def get_data(connection, target_vm_name=None):
    """
    Obtain data of `target_vm_name` if specified, otherwise obtain data of all vms.
    """
    all_vms_name_list = connection.listAllDomains()
    active_vms_id_list = connection.listDomainsID()
    active_vms_name_list = []
    if len(active_vms_id_list) != 0:
        for vmID in active_vms_id_list:
            vm = connection.lookupByID(vmID)
            active_vms_name_list.append(vm.name())

    ### UPDATE for Single VM ###
    if target_vm_name:
        data = get_dict_of_struct(
            connection=connection,
            target_vm_name=target_vm_name,
        )

    ### UPDATE for Multiple VMs ###
    else:
        vms = dict()
        data = defaultdict(list)
        for vm in all_vms_name_list:
            name = vm.name()

            # Add vm to vms dict
            vms[name] = get_dict_of_struct(connection, name)

        data["_meta"] = {
            'hostvars': vms,
        }
    ################################
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
