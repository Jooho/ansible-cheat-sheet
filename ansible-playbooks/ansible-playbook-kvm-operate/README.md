Ansible Playbook: Clone/Attach storage/Operate VM on KVM
=========

This playbook help run to Jooho.kvm_oeprate role. 

Requirements
------------
None

Dependencies
------------

- [Jooho.kvm_operate](https://galaxy.ansible.com/Jooho/kvm_operate/)



Role Variables
--------------

| Name             | Default value | Requird | Description                                                                         |
| ---------------- | ------------- | ------- | ----------------------------------------------------------------------------------- |
| kvm_install_host | localhost     | no      | KVM install host                                                                    |
| kind             | undefined     | yes     | Set vm for start/stop/suspend/destory/teardown Or set storage for attach extra disk |
| operate          | undefined     | yes     | Set start/stop/suspend/destory/teardown for vm Or attach for storage                |
| src_vm           | undefined     | yes     | Clone operate params. The base vm name                                              |
| dest_vm          | undefined     | yes     | Clone operate params. A new vm name                                                 |
| dest_vm_hostname | undefined     | no      | Clone operate params. Set hostname if you want to update hostname                   |
| vm_network_br    | default       | no      | Set if cloned vm use differen br                                                    |
| prefix_vm        | undefined     | yes     | start/stop/suspend/destory/clone params. For multiple VMs                           |
| vm_name          | undefined     | yes     | start/stop/suspend/destory/clone. For single VM                                     |
| target_vm        | undefined     | yes     | Storage params. Attach VM name                                                      |
| disk_size        | undefined     | yes     | Storage params. A new disk size (ex, 20G/200M)                                      |


Example Var override
--------------------
```
    - import_role:
        name: Jooho.kvm_operate
      vars:
        kvm_vm_pool_dir: /home/jooho/KVM
```        


Example Execute Command
-----------------------

- Download roles
~~~
ansible-galaxy install -f -r requirements.yaml
~~~

- Execute playbook
~~~
ansible-playbook -i /etc/ansible/hosts playbook.yaml
~~~


License
-------

BSD

Author Information
------------------

This role was created in 2018 by [Jooho Lee](http://github.com/jooho).

