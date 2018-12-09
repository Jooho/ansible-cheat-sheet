Ansible Playbook: KVM Provider for OKD
=========

This playbook help run to Jooho.kvm-provider-okd role. 


Requirements
------------
None

Dependencies
------------

- [Jooho.kvm-provider-okd](https://galaxy.ansible.com/Jooho/kvm-provider-okd/)

Roles Variables
--------------
| Name             | Default value        | Requird | Description                              |
| ---------------- | -------------------- | ------- | ---------------------------------------- |
| kvm_log_dir      | /tmp/kvm             | no      | Where role related config/log file store |
| kvm_vm_pool_dir  | /var/lib/virt/images | no      | Where VM images store                    |
| kvm_install_host | localhost            | no      | Where KVM will install or installed      |


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

BSD/MIT

Author Information
------------------

This role was created in 2018 by [Jooho Lee](http://github.com/jooho).

