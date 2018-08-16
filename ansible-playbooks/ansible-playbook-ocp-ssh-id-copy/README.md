Ansible Playbook: Openshift SSH ID COPY
=========

This playbook demonstrate how to use Jooho.ansible-role-ssh-id-copy role
It copies ssh public key to a node.


Requirements
------------
None

Dependencies
------------

- [Jooho.ansible_role_ocp_ssh_id_copy](https://galaxy.ansible.com/Jooho/ansible_role_ocp_ssh_id_copy)

Roles Variables
--------------

| Name                      | Default value                         |        Requird       | Description                                                                 |
|---------------------------|---------------------------------------|----------------------|-----------------------------------------------------------------------------|
| ssh_id_copy_target        | cluster (new_nodes, real_ip)          |         yes          | If single ip is set, it copies a public key to the specific host            |
|                           |                                       |                      | cluster - use all_nodes group, new_nodes use new_nodes group                |
| ssh_public_key            | /root/.ssh/id_rsa.pub                 |         yes          | Public key that will be copied                                              |
| target_vm.id              | test                                  |         yes          | User Id to access target host                                               |
| target_vm.pw              | test                                  |         yes          | User Password to access target host                                         |

**NOTE**
If you want to use different vars from default one, you should specify them with -e options

Example Execute Commands
-----------------------

- **Download roles**
~~~
cd ansible-cheat-sheet/ansible-playbooks/ansible-playbook-ocp-ssh-id-copy

$ ansible-galaxy install -f -r requirements.yaml -p ./roles
~~~

- **Use var file**

~~~
$ vi vars/main.yml

target_vm:
  id: "root"
  pw: "root"


ssh_public_key: "/root/.ssh/id_rsa.pub"
ssh_id_copy_target: test.example.com


$ ansible-playbook -i /path/to/hosts ./playbook.yaml                           
~~~

- **Use inline var value**
```
$ ansible-playbook -i /path/to/hosts  ./playbook.yaml -e '{base_image: {id: root, pw: root}}'
```

Quick Demo Script
----------------
### Basic Setup
```
git clone https://github.com/Jooho/ansible-cheat-sheet.git

cd ansible-cheat-sheet/ansible-playbooks/ansible-playbook-ocp-ssh-id-copy

ansible-galaxy install -f -r requirements.yaml -p ./roles

source ./setup  (* Update setup file)
```

### Example single node
```
ansible-playbook -i ./hosts ./playbook-single.yaml -e ssh_id_copy_target=$TARGET_HOSTNAME

Tip:
   ansible-playbook -i ./hosts ./playbook-single.yaml -e '{base_image: {id: root, pw: root}}'
```

### Example multiple nodes

```
ansible-playbook -i ./hosts ./playbook-multiple.yaml

or

ansible-playbook -i ./hosts ./playbook-multiple.yaml -e @vars/main.yml

```

Sample Hosts file
------------------

```
ssh_public_key: "{{lookup('env', 'SSH_PUBLIC_KEY')}}"

target_vm:
  id: "{{lookup('env', 'TARGET_VM_ID')}}"
  pw: "{{lookup('env', 'TARGET_VM_PW')}}"

[masters]
master1.example.com

[etcd]
master1.example.com

[nodes]
master1.example.com openshift_node_labels="{'region': 'mgmt', 'role': 'master'}"
node1.example.com   openshift_node_labels="{'region': 'infra', 'role': 'app', 'zone': 'default'}"
node2.example.com   openshift_node_labels="{'region': 'infra', 'role': 'app', 'zone': 'default'}"
```

Video Clip
----------
[![asciicast](https://asciinema.org/a/144986.png)](https://asciinema.org/a/144986)


Result Image
------------
![alt Result](./result.png)

License
-------

BSD/MIT

Author Information
------------------

This role was created in 2018 by [Jooho Lee](http://github.com/jooho).

