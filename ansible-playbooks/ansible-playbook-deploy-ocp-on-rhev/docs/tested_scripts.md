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
| Common Command | deploy.py |
| deploy cluster | -e deploy_type=ocp -e  operate=deploy |
| deploy cluster | -e deploy_type=ocp -e  operate=deploy -e tag=35-1012|
| deploy cluster | -e deploy_type=ocp -e  operate=deploy -e tag=35-1012 -e ocp_version=3.5|
| stop single node | -e deploy_type=ocp -e operate=stop -e tag=35-1012 -e target_node_filter=infra_1 |
| stop ocp cluster | -e deploy_type=ocp -e operate=stop -e tag=35-1012 |
| start single node | -e deploy_type=ocp -e operate=start -e target_cluster_tag=35-1012 -e target_node_filter=infra_1 |
| start ocp cluster | -e deploy_type=ocp -e operate=start -e target_cluster_tag=35-1012 |
| teardown vms not installed ocp|  -e deploy_type=ocp -e  operate=teardown -e target_cluster=351012 -e ocp_install=false|
| teardown vms installed ocp |  -e deploy_type=ocp -e  operate=teardown -e target_cluster=35-1012 -e ocp_install=true|
| scale up single infra node   |-e deploy_type=scale -e operate=up -e target=infra|
| scale up multiple infra nodes   |-e deploy_type=scale -e operate=up -e target=infra -e instances=2|
| scale up single app node   |-e deploy_type=scale -e operate=up -e target=app|
| scale up single app nodes   |-e deploy_type=scale -e operate=up -e target=app -e instances=2|
| bluegreen upgrade master | -e deploy_type=bg_upgrade -e target=master |
| bluegreen upgrade node | --deploy_type=bg_upgrade --target=node --operate=deploy --ocp_version=3.6 --new_cluster_color=green --tag=35-1012  |
| bluegreen warmup node | --deploy_type=bg_upgrade --target=node --operate=warmup  --new_cluster_color=green   |

### Command Syntax

>$Commom_Command $Sub_Command

```
deploy.py -e deploy_type=ocp -e operate=deploy
```

