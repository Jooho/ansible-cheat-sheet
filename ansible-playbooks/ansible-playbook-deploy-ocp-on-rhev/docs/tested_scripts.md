Tested Scripts
--------------


Architecture (1 LB x 3 Master x 3 Infa x 2 App)


| Main Command|         Scenario       | Result|
|--------|------------------------|-------|
| deploy |  cluster               |   O  (50mins ~ 1 hours) |
| stop   |  single node           |   O   |
| stop   |  multiple nodes        |   O   |
| stop   |  ocp cluster           |   O   |
| start  |  single node           |   O   |
| start  |  multiple nodes        |   O   |
| start  |  ocp cluster           |   O   |
| teardown| vm not installed ocp  |   O   |
| teardown| vm installed ocp      |   O   |
| scale up | single infra/app node    |   O   |
| scale up | multiple infra/app nodes |   O   |
| scale down | single infra/app node  |   O   |
| scale down | multiple infra/app nodes |   O   |
| bluegreen upgrade | master servers(including etcd) | O |
| bluegreen upgrade | create new vms and install version of infra/app nodes | O |




| Main Command Type|Practise command        |
|--------|--------|
| Common Command | ansible-playbook playbooks/config.yaml -M ./modules -i ./inventory/rhev/hosts/rhev.py -e @vars/all -e @vars/ocp_params -e provider=rhev 
| deploy cluster | -e deploy_type=ocp -e  operate=deploy |
| deploy cluster | -e deploy_type=ocp -e  operate=deploy -e tag=34-0912|
| deploy cluster | -e deploy_type=ocp -e  operate=deploy -e tag=34-0912 -e ocp_version=3.5|
| stop single node | -e deploy_type=ocp -e operate=stop -e target_cluster_tag=34-0912 -e target_node_filter=infra_1 |
| stop ocp cluster | -e deploy_type=ocp -e operate=stop -e target_cluster_tag=34-0912 |
| start single node | -e deploy_type=ocp -e operate=stop -e target_cluster_tag=34-0912 -e target_node_filter=infra_1 |
| start ocp cluster | -e deploy_type=ocp -e operate=stop -e target_cluster_tag=34-0912 |
| teardown vms not installed ocp|  -e deploy_type=ocp -e  operate=teardown -e target_cluster=34-0912 -e ocp_install=false|
| teardown vms installed ocp |  -e deploy_type=ocp -e  operate=teardown -e target_cluster=34-0912 -e ocp_install=true|
| scale up single infra node   |-e deploy_type=scale -e operate=up -e scale_target=infra|
| scale up multiple infra nodes   |-e deploy_type=scale -e operate=up -e scale_target=infra -e instances=2|
| scale up single app node   |-e deploy_type=scale -e operate=up -e scale_target=app|
| scale up single app nodes   |-e deploy_type=scale -e operate=up -e scale_target=app -e instances=2|
| bluegreen upgrade master | -e deploy_type=bg_upgrade -e target=master |
| bluegreen upgrade node | -e deploy_type=bg_upgrade -e target=node  -e operate=deploy  |
| bluegreen upgrade node | -e deploy_type=bg_upgrade -e target=node  -e operate=deploy  |

### Command Syntax

>$Commom_Command $Sub_Command

```
ansible-playbook playbooks/config.yaml -M ./modules -i ./inventory/rhev/hosts/rhev.py -e @vars/all -e @vars/ocp_params -e provider=rhev -e deploy_type=ocp -e  operate=deploy
```

