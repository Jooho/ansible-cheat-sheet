Ansible Controller VM
---------------------

*Description*

  This help create RHEV VM from base template and it will install essential packages/git repositories.
  For deploying openshift cluster, you should create Ansible Controller. Moreover, 

*Files*
- playbooks/rhev/ansible-controller.yaml

*Pre-requisites*
- [Create base rhel image](./base-rhel-image.md)
- [Create ocp base template](./base-rhel-ocp-template.md)

*Related Docs*
- [Download RHEV Cert](./download-rhev-cert.md)
- [Credential Information](./setup.md)


*Manaual Way*
Commands for Requirement on local system
```
yum install ansible -y

wget https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
chmod 777 /tmp/get-pip.py
python /tmp/get-pip.py
pip install ovirt-engine-sdk-python 

```

*Ansible Way*

```
ansible-playbook playbooks/rhev/ansible-controller.yaml -e @vars/all -e ocp_version=3.6

cd /root/git/ansible-cheat-sheet/ansible-playbooks/ansible-playbook-deploy-ocp-on-rhev
```

*Video Clips:*

[![asciicast](https://asciinema.org/a/142052.png)](https://asciinema.org/a/142052)
[![asciicast](https://asciinema.org/a/142059.png)](https://asciinema.org/a/142059)
