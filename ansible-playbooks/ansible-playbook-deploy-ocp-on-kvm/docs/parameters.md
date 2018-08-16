Parameters
----------

There are mainly 2 variable files
- vars/all
- vars/ocp_params

Literally, ocp_params has ocp related variable like normal ocp hosts file but only 3 params are inherited from vars/all.
- openshift_master_default_subdomain
- openshift_master_cluster_hostname
- openshift_master_cluster_public_hostname

The main variables are specified in vars/all.

*RHEV VM Basic Info*

| variable| default | description |
|---------|---------|-------------|
|prefix_vm|  jlee   | This value will be used for vm name prefix                                     |
|tag      | 34-0912 | If set, it overwrite cluster_tag which is ocp_version + timestamp('date +%m%d')|
|         |         | This is used for specifying cluster when multiple cluster exist.               |


*Base Image Info*

|       variable        | default | description |
|-----------------------|---------|-------------|
|base_image.os          |   rhel  |  OS Type    |           
|base_image.version     |   7u3   |  OS Version |
|base_image.rhev_os_type|   7x64  |  OS Type in RHEV|


*OCP Info*

|     variable     | default | description |
|------------------|---------|-------------|
|ocp_version       | 3.4     |                                                                      |
|ocp_dns_domain    | gsslab.rdu2.redhat.com|                                                        | 
|master_node_vms   | 3       | Master nodes. If it is more than 1, lb will be deployed automatiaclly|
|infra_node_vms    | 3       | Infra Nodes                                                          | 
|app_node_vms      | 2       | App Nodes                                                            | 
|master_node_prefix| master  | Master node noticable prefix                                         |
|infra_node_prefix | infra   | Infra node noticable prefix                                          |
|app_node_prefix   | app     | App node noticable prefix                                            |
|etcd_node_prefix  | etcd    | ETCD node noticable prefix                                           |
|lb_node_prefix    | lb      | lb node noticable prefix                                             |

**notice**
ETCD can not be installed from Masters but it is not tested yet.


*ETC Info*

|         variable        | default   | description |
|-------------------------|-----------|-------------|
|loglevel                 | info      | If set debug, it shows debug log for dynamic variables|
|interim_dns.install      | true      | intermin dns is dnsmasq for setting master internal/external url. If you have external DNS or LB, you can set it false.|
|                         |           | But you should configure your own LB or DNS before deploying ocp. LB and Master internal/external url should be resolvable by them|
|interim_dns.forwarder_dns| 10.11.5.4 | This should be RHEV DNS that can resolve VM hostname.|




Reference: 
- [Credential Information](./setup.md) 

