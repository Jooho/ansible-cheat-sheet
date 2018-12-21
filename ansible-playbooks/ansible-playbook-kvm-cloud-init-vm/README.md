Ansible Playbook: Deploy cloud init image on KVM
=========

This playbook help run to Jooho.kvm_cloud_init_vm role. 


Requirements
------------
None

Dependencies
------------

- [Jooho.kvm_cloud_init_vm](https://galaxy.ansible.com/Jooho/kvm_cloud_init_vm/)

Roles Variables
--------------

| Name                     | Default value                                                                    | Requird | Description                                                |
| ------------------------ | -------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------- |
| kvm_vm_pool_dir          | /var/lib/virt/images                                                             | no      | The path where KVM VM images are stored                    |
| vm_data_dir              | /root/kvm/vms                                                                    | no      | The path where VM information are stored                   |
| vm_recreate              | true                                                                             | no      | Set false, if the same vm exist                            |
| cloud_init_vm_image      | CentOS-7-x86_64-GenericCloud.qcow2                                               | no      | Cloud init image name                                      |
| cloud_init_vm_image_link | https://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud-1809.qcow2 | no      | Cloud init image download link                             |
| cloud_init_user_data     | {{vm_data_dir}}/{{vm_name}}/user-data                                            | no      | Cloud init user data file                                  |
| cloud_init_meta_data     | {{vm_data_dir}}/{{vm_name}}/meta-data                                            | no      | Cloud init meta data file                                  |
| cloud_init_iso_image     | {{vm_data_dir}}/{{vm_name}}/cidata.iso                                           | no      | Cloud init booting image                                   |
| vm_name                  | CentOS_Base                                                                      | no      |                                                            |
| vm_local_hostname        | base.example.com                                                                             | no      | VM internal hostname(it can be the same with vm_hostname)  |
| vm_hostname              | base.example.com                                                                 | no      | VM public hostname                                         |
| vm_public_key            | {{lookup('file','~/.ssh/id_rsa.pub')}}                                           | no      | SSH public key to login to the VM(ocp/redhat,centos/(ssh)) |
| vm_cpu                   | 2                                                                                | no      |                                                            |
| vm_memory                | 2048                                                                             | no      |                                                            |
| vm_network_br            | virbr0                                                                       | no      | Default bridge name that the VM will use                   |
| vm_root_disk_size        | 20G                                                                              | no      |                                                            |

Example Var override
--------------------
```
    - import_role:
        name: Jooho.kvm-cloud-init-vm
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

