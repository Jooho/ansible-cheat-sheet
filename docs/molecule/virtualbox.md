# Molecule with VirtualBox using vagrant

Environment
-----------

OS: Fedora/Centos/RHEL


## How to use virtualbox


Create a role without --driver (vagrant is default)
--------------------

~~~
molecule init --role ansible-role
~~~

Default molecule.yml
-------------------

~~~
dependency:
  name: galaxy
driver:
  name: vagrant
vagrant:
  platforms:
    - name: ubuntu/trusty64
      box: trusty64
      box_url: https://vagrantcloud.com/ubuntu/boxes/trusty64/versions/14.04/providers/virtualbox.box
  providers:
    - name: virtualbox
      type: virtualbox
      options:
        memory: 512
        cpus: 2
  instances:
    - name: test-role-vagrant
      ansible_groups:
        - group1
verifier:
  name: testinfra
~~~

Add centos/7 box
---------------
~~~
...
platforms:
    - name: ubuntu/trusty64
      box: trusty64
      box_url: https://vagrantcloud.com/ubuntu/boxes/trusty64/versions/14.04/providers/virtualbox.box
    - name: centos
      box: centos/7
...
~~~

Execute molucule test
---------------------
~~~
molecule test --platform centos   

--> Destroying instances...
--> Checking playbook's syntax...

playbook: playbook.yml
--> Creating instances...
Bringing machine 'test-role-vagrant' up with 'virtualbox' provider...
==> test-role-vagrant: Box 'centos/7' could not be found. Attempting to find and install...
    test-role-vagrant: Box Provider: virtualbox
    test-role-vagrant: Box Version: >= 0
==> test-role-vagrant: Loading metadata for box 'centos/7'
    test-role-vagrant: URL: https://atlas.hashicorp.com/centos/7
==> test-role-vagrant: Adding box 'centos/7' (v1705.02) for provider: virtualbox
    test-role-vagrant: Downloading: https://app.vagrantup.com/centos/boxes/7/versions/1705.02/providers/virtualbox.box
==> test-role-vagrant: Successfully added box 'centos/7' (v1705.02) for 'virtualbox'!
==> test-role-vagrant: Preparing master VM for linked clones...
    test-role-vagrant: This is a one time operation. Once the master VM is prepared,
    test-role-vagrant: it will be used as a base for linked clones, making the creation
    test-role-vagrant: of new VMs take milliseconds on a modern system.
==> test-role-vagrant: Importing base box 'centos/7'...
...
~~~

## Tip

SSH key insert: false
-------------------
~~~
vagrant:
  raw_config_args:
  - "ssh.insert_key = false"
~~~


## Reference
- [Vagrant Box Search](https://app.vagrantup.com/)

Author Information
------------------

This role was created in 2017 by [Jooho Lee](http://github.com/jooho).

