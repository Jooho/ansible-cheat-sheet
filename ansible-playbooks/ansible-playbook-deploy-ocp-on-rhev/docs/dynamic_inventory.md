Dynamic Inventory Hosts 
-----------------------

This Ansible script use dynamic inventory host file like aws(ec2.py/ec2.ini). The original upsteam file is customized to load os enviroment for credential.

Basically, inventory file gather all vm information so if there are many vms, it takes time. Hence, this [customerized file](../inventory/rhev/hosts/ovirt.py) has a feature to filter vms with [vm_filter](../inventory/rhev/hosts/ovirt.ini) parameter. 

This vm_filter should be prefix of vm name.

**Example**
*inventory/rhev/hosts/ovirt.ini*
```
vm_filter=jlee
```

It will gather only vms begin with jlee like following:
```
jlee_34-0912_RHEL7U3_OCP3U4_master_1
jlee_34-0912_RHEL7U3_OCP3U4_master_2
...
```


Execute dynamic inventory hosts 
```
inventory/rhev/hosts/ovirt.py --pretty
```

Reference:
- [Upstream Ovirt Dynamic Inventory Hosts](https://fossies.org/linux/ansible/contrib/inventory/rhv.py)
