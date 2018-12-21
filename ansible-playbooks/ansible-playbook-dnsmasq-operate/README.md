Ansible Playbook: DNSmasq operate 
=========

This playbook help run to Jooho.dnsmasq_operate role. 


Requirements
------------
None

Dependencies
------------

- [Jooho.dnsmasq_operate](https://galaxy.ansible.com/Jooho/dnsmasq_operate/)

Roles Variables
--------------

| Name                 | Default value  | Requird | Description                                                                  |
| -------------------- | -------------- | ------- | ---------------------------------------------------------------------------- |
| dns_conf_name        | undefined      | yes     | dnsmasq conf file (/etc/dnsmasq.d/file.conf)                                 |
| dns_conf_path        | /etc/dnsmasq.d | no      | dnsmasq conf path                                                            |
| rewrite_conf         | true           | no      | Set false if you don't want to overwrite conf file when it exists            |
| forward_dns          | 8.8.8.8        | no      | Set upstream DNS nameservers                                                 |
| rewrite_forward_conf | false          | no      | Set true if upstream DNS nameservers are changed                             |
| dns_ops              | install        | no      | Set install for dnsmasq package, add/remove for address or nameserver        |
| new_ip               | undefined      | yes     | For address record, it will map to new_hostname or new_nameserver_search_for |
| new_hostname         | undefined      | yes     | For address record, it will map to new_ip                                    |
| new_ns_search_for    | undefined      | yes     | For nameserver recode, it will map to new_ip                                 |

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

