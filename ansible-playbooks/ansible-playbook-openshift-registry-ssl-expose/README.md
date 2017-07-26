Ansible Playbook: Openshift Docker Registry Securing and Exposing Service
=========

This role help create a custom certificate for openshift integrated docker registry and apply the cert on docker registry.
Then, expose docker registry service to accept external access

Requirements
------------
None

Dependencies
------------

- [Jooho.openshift-registry-ssl-expose](https://galaxy.ansible.com/Jooho/openshift-registry-ssl-expose/)


Example Execute Command
-----------------------
~~~
ansible-galaxy install -f Jooho.openshift-registry-ssl-expose

ansible-playbook playbook.yaml  -e docker_registry_route_url='docker-registry.cloudapps.example.com' -e docker_registry_svc_name=docker-registry  -e docker_registry_svc_ip=172.30.210.68  -e replace_cert=true  -e restart_docker=true 
~~~

Test Shell Script
-----------------
Refer [Test Shell Script](https://github.com/Jooho/ansible-role-openshift-registry-ssl-expose/blob/master/README.md)

License
-------

BSD/MIT

Author Information
------------------

This role was created in 2017 by [Jooho Lee](http://github.com/jooho).

