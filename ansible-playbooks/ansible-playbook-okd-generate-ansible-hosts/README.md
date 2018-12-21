Ansible Playbook: Generate Ansible Hosts for OKD installation
=========

This playbook help run to Jooho.okd_generate_ansible_hosts role. 


Requirements
------------
None

Dependencies
------------

- [Jooho.okd_generate_ansible_hosts](https://galaxy.ansible.com/Jooho/okd_generate_ansible_hosts/)

Roles Variables
--------------


| Name                            | Default value      | Requird | Description                                                                     |
| ------------------------------- | ------------------ | ------- | ------------------------------------------------------------------------------- |
| okd_param_name                  | okd_param          | no      | okd param file name                                                             |
| okd_official_param_name         | okd_param_official | no      | okd official param file name that is converted from official ansible hosts file |
| okd_param_dir                   | undefined          | yes     | Directory path where okd param file is                                          |
| okd_official_ansible_hosts_name | okd_official_hosts | no      | official ansible hosts file name. It will be stored uder okd_param_dir          |
| cluster_tag                     | undefined          | yes     | For backup, need to specify tag (ex OKD0311)                                    |
| reformat_vars_to_hosts          | true               | no      | Set false if you want to convert official hosts file to varible style           |


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

