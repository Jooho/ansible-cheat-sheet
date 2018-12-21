Ansible Playbook: Prerequisites for OKD installation
=========

This playbook help run to Jooho.okd_prerequisites role. 


Requirements
------------
None

Dependencies
------------

- [Jooho.okd_prerequisites](https://galaxy.ansible.com/Jooho/okd_prerequisites/)

Roles Variables
--------------

| Name                | Default value | Requird | Description                                                 |
| ------------------- | ------------- | ------- | ----------------------------------------------------------- |
| node_type           | undefined     | yes     | OKD host type(okd-host or okd-lb)                           |
| okd_version         | 3.11          | no      | OKD version                                                 |
| docker_version      | 1.13.1        | no      | Docker version                                              |
| docker_storage_disk | vdb           | no      | Disk name for docker storage(ex, vdc)                       |
| interim_dns_use     | false         | no      | Set true, if you set interim dns                            |
| interim_dns_ip      | undefined     | yes     | If you set true to interim_dns_use, you must set this value |


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

