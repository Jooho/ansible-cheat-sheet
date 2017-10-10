Deploy OpenShift Container Platform on Premise
---------------------------------------------

### Steps
- Download [RHEV certificate](./download-rhev-cert.md)
- Update [Parameters](./parameters.md)
- Update [Credential Information](./docs/setup.md)
- Update [OCP variables](../vars/ocp_params)

 

### Execute this command ###
```
# If you already did it, you can skip it
source ~/setup

ansible-playbook playbooks/config.yaml -M ./modules -i ./inventory/rhev/hosts/ovirt.py -e @vars/all -e @vars/ocp_params -e provider=rhev -e deploy_type=ocp -e  operate=deploy 
```
