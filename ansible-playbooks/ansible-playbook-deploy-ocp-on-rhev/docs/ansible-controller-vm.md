Ansible Controller VM
---------------------

Ansible Controller VM need to install essential packages

**Requirement**
- ansible 2.4.0
- ovirt-engine-sdk-python


Commands for Requirement on local system
```
wget https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
chmod 777 /tmp/get-pip.py
python /tmp/get-pip.py
pip install ovirt-engine-sdk-python 
pip install ansible==2.4
```

Ansible script for creating ansible controller vm.
```
ansible-playbook playbooks/rhev/ansible-controller.yaml -e @vars/all -e ocp_version=3.6

cd /root/git/ansible-cheat-sheet/ansible-playbooks/ansible-playbook-deploy-ocp-on-rhev
```


The path of ansible : **/root/git/ansible-cheat-sheet/ansible-playbooks/ansible-playbook-deploy-ocp-on-rhev**
