Ansible Playbook: Openshift SSH ID COPY
=========

This playbook demonstrate how to use Jooho.copy-ssh-pub-key role
It copies ssh public key to a VM or VMs.

Requirements
------------
- sshpass

Dependencies
------------

- [Jooho.copy_ssh_pub_key](https://galaxy.ansible.com/Jooho/copy_ssh_pub_key)

Roles Variables
--------------

| Name           | Default value         | Requird | Description                                                  |
| -------------- | --------------------- | ------- | ------------------------------------------------------------ |
| target_vm      | undefined             | yes     | Single VM. it copies a public key to the specific host       |
| target_vms     | undefined             | yes     | Multiple VMs. it copies a public key to the multiple hosts   |                                 
| ssh_public_key | /root/.ssh/id_rsa.pub | yes     | Public key that will be copied                               |
| target_vm_id   | test                  | yes     | User Id to access target host                                |
| target_vm_pw   | test                  | yes     | User Password to access target host                          |

Example Execute Commands
-----------------------

- **Download roles**
~~~
cd ansible-cheat-sheet/ansible-playbooks/ansible-playbook-copy-ssh-pub-key

$ ansible-galaxy install -f -r requirements.yaml -p ./roles
~~~

- **Example Vars**

Using environment variable for credentials
~~~
$ vi vars/main.yml

target_vm: test.example.com
ssh_public_key: "{{lookup('file', 'SSH_PUBLIC_KEY')}}"
target_vm_id: "{{lookup('env', 'TARGET_VM_ID')}}"
target_vm_pw: "{{lookup('env', 'TARGET_VM_PW')}}"


$ ansible-playbook -i /path/to/hosts ./playbook.yaml                           
~~~

Using plain text for credentials
~~~
$ vi vars/main.yml

target_vms:
- 192.168.200.2
- 192.168.200.3
target_vm_id: "root"
target_vm_pw: "root"

ssh_public_key: "/root/.ssh/id_rsa.pub"

$ ansible-playbook -i /path/to/hosts ./playbook.yaml                           
~~~


Quick Demo Script
----------------
### Basic Setup
```
git clone https://github.com/Jooho/ansible-cheat-sheet.git

cd ansible-cheat-sheet/ansible-playbooks/ansible-playbook-copy-ssh-pub-key

ansible-galaxy install -f -r requirements.yaml -p ./roles

```

### Example single node
```
ansible-playbook -i ./hosts ./playbook.yaml -e target_vm=10.10.124.13 -e @vars/main.yml

```

### Example multiple nodes

```
# hosts file has to be updated before execute below command

ansible-playbook -i ./hosts ./playbook.yaml -e @vars/main.yml

```

Video Clip
----------
None


License
-------

BSD

Author Information
------------------

This role was created in 2018 by [Jooho Lee](http://github.com/jooho).

