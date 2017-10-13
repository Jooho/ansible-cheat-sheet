Deploy OpenShift Container Platform on Premise
---------------------------------------------

*Description*

Using ansible, it will create VMs on RHEV and it will install OCP. Before execute ansible script, you should update parameters for [RHEV](./parameters.md) and [OCP]((../vars/ocp_params). 

*Pre-requisites*
- [Create base rhel image](./base-rhel-image.md)
- [Create ocp base template](./base-rhel-ocp-template.md)
- [Set up ansible controller vm](./ansible-controller-vm.md)


*Related Docs*
- [Download RHEV Cert](./download-rhev-cert.md)
- [Credential Information](./setup.md)
- [Parameters](./parameters.md)


*Demo Scenario*
 - Architecture : 3 x Master, 3 x Infra, 2 x App, LB
 - ocp_version: 3.5
 - tag: 35-1012
 - prefix_vm: jlee
 - interim_dns.install: yes
 

*Commands on ansible controller* 

```
source ~/setup

./deploy.py --deploy_type=ocp --operate=deploy --force=true  
```
*Video Clips*

[![asciicast](https://asciinema.org/a/142266.png)](https://asciinema.org/a/142266)
[![asciicast](https://asciinema.org/a/142298.png)](https://asciinema.org/a/142298)
