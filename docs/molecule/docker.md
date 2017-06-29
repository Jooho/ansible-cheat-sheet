# Molecule with Docker

Environment
-----------

OS: Fedora/Centos/RHEL


## How to use docker


Create a role with --driver=docker
--------------------

~~~
molecule init --role test-role-docker --driver=docker
~~~

Default molecule.yml
-------------------

~~~
dependency:
  name: galaxy
driver:
  name: docker
docker:
  containers:
    - name: test-role-docker
      image: ubuntu
      image_version: latest
      ansible_groups:
        - group1
verifier:
  name: testinfra
~~~

Add centos Image
---------------
~~~
...
docker:
  containers:
    - name: test-role-docker
      image: ubuntu
      image_version: latest
      ansible_groups:
        - group1
    - name: test-role-docker-centos
      image: centos
      image_version: latest
...
~~~

Execute molucule test
---------------------

The ansible script will execute on both containers.

~~~
molecule test 

--> Destroying instances...
--> Checking playbook's syntax...

playbook: playbook.yml
--> Creating instances...
--> Creating Ansible compatible image of ubuntu:latest ...
Creating container docker-ubuntu with base image ubuntu:latest...
Container created.
--> Creating Ansible compatible image of centos:latest ...
Creating container docker-centos with base image centos:latest...
Container created.
--> Starting Ansible Run...

...
~~~

## Tip


Author Information
------------------

This role was created in 2017 by [Jooho Lee](http://github.com/jooho).

