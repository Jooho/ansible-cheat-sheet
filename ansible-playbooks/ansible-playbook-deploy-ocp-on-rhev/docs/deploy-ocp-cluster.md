Deploy OpenShift Container Platform on Premise
---------------------------------------------

*Description*

Using ansible, it will create VMs on RHEV and it will install OCP. Before execute ansible script, you should update parameters for [RHEV](./parameters.md) and [OCP]((../vars/ocp_params). 

*Pre-requisites*
- [Create base rhel image](./base-rhel-image.md)
- [Create ocp base template](./base-rhel-ocp-template.md)
- [Set up ansible controller vm](./ansible-controller-vm.md)


*Related Docs*
- [Download RHEV Cert](./docs/download-rhev-cert.md)
- [Parameters](./docs/parameters.md)
- [Credential Information](./docs/setup.md)

*Demo Scenario*
 - Architecture : 3 x Master, 3 x Infra, 2 x App, LB
 - ocp_version: 3.5
 - tag: 35-1012
 - prefix_vm: jlee
 - interim_dns.install: yes
 

*Commands on ansible controller* 

```
source ~/setup

ansible-playbook playbooks/config.yaml -M ./modules -i ./inventory/rhev/hosts/ovirt.py -e @vars/all -e @vars/ocp_params -e provider=rhev -e deploy_type=ocp -e  operate=deploy 
```
