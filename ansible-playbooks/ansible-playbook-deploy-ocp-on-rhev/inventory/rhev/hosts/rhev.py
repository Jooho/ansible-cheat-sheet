#!/usr/bin/env python

'''
Example custom dynamic inventory script for Ansible, in Python.
'''

import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json

class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print json.dumps(self.inventory, sort_keys=True, indent=2);

    # Example inventory for testing.
    def example_inventory(self):
        return {
            "tag_Name_34_0912_master_node": [
                "dhcp181-61.gsslab.rdu2.redhat.com",
                "dhcp182-163.gsslab.rdu2.redhat.com"
            ],
            "tag_Name_34_0912_lb_node": [
                "dhcp181-99.gsslab.rdu2.redhat.com",
            ],
            "tag_Name_34_0912_infra_node": [
                "dhcp182-189.gsslab.rdu2.redhat.com",
            ],
            "tag_Name_34_0912_app_node": [
                "dhcp181-93.gsslab.rdu2.redhat.com",
            ],
            "_meta": {
                "hostvars": {
                    "dhcp181-61.gsslab.rdu2.redhat.com": {
                        "ansible_host": "dhcp181-61.gsslab.rdu2.redhat.com"
                    },

                    "dhcp182-163.gsslab.rdu2.redhat.com": {
                        "ansible_host": "dhcp182-163.gsslab.rdu2.redhat.com"
                    },

                    "dhcp181-99.gsslab.rdu2.redhat.com": {
                        "ansible_host": "dhcp181-99.gsslab.rdu2.redhat.com"
                    },

                    "dhcp182-189.gsslab.rdu2.redhat.com": {
                        "ansible_host": "dhcp182-189.gsslab.rdu2.redhat.com"
                    },

                    "dhcp181-93.gsslab.rdu2.redhat.com": {
                        "ansible_host": "dhcp181-93.gsslab.rdu2.redhat.com"
                    }

                }
            }
        }

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
ExampleInventory()
