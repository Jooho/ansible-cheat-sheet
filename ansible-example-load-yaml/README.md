Ansible Example : Load Yaml File
=========

This example show how to load yaml file and how to use each value as var in role or playbook


Requirements
------------
- Molecule
- Docker or VirtualBox

Dependencies
------------

None

Execute  Playbook
----------------
~~~
molecule test
~~~

Sample Yaml 
------------
~~~
first_value: "The First Value"
zones:
  - name: named.example-com
    hosts:
    - name: master1
      ip: 192.168.200.200
    - name: master2
      ip: 192.168.200.201

  - name: named.cloudapps-example-com
    hosts:
      - name: "*"
        ip:
          - 192.168.200.201
          - 192.168.200.202
~~~

Example 
-----------

- Get root var 
- Get zones list 
- Get first list of zones
- Get name value from first list value of zones
- Get name/ip of hosts of all zones list 

License
-------

BSD/MIT

Author Information
------------------

This role was created in 2017 by [Jooho Lee](http://github.com/jooho).

