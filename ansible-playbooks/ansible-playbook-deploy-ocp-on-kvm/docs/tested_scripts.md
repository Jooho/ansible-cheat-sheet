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
| bluegreen upgrade | master servers(including etcd) | testing |
| bluegreen upgrade | create new vms and install version of infra/app nodes | testing |
| bluegreen warmup  | Get latest templates/images | testing |
| metrics deploy    | deploy metrics component   | O |
| metrics undeploy  | undeploy metrics component | O |
| metrics upgrade   | upgrade metrics component  | testing |
| logging deploy    | deploy logging component   | O |
| logging undeploy  | undeploy logging component | O |
| logging upgrade   | upgrade logging component  | testing |




| Main Command Type|Practise command        |
|--------|--------|
| Common Command | deploy.py |
| deploy cluster | --deploy_type=ocp --operate=deploy |
| deploy cluster | --deploy_type=ocp -- operate=deploy --tag=35-1012|
| deploy cluster | --deploy_type=ocp -- operate=deploy --tag=35-1012 --ocp_version=3.5|
| stop single node | --deploy_type=ocp --operate=stop --tag=35-1012 --target_node_filter=infra_1 |
| stop ocp cluster | --deploy_type=ocp --operate=stop --tag=35-1012 |
| start single node | --deploy_type=ocp --operate=start --target_cluster_tag=35-1012 --target_node_filter=infra_1 |
| start ocp cluster | --deploy_type=ocp --operate=start --target_cluster_tag=35-1012 |
| teardown vms not installed ocp|  --deploy_type=ocp -- operate=teardown --target_cluster=351012 --ocp_install=false|
| teardown vms installed ocp |  --deploy_type=ocp -- operate=teardown --target_cluster=35-1012 --ocp_install=true|
| scale up single infra node   |--deploy_type=scale --operate=up --target=infra|
| scale up multiple infra nodes   |--deploy_type=scale --operate=up --target=infra --instances=2|
| scale up single app node   |--deploy_type=scale --operate=up --target=app|
| scale up single app nodes   |--deploy_type=scale --operate=up --target=app --instances=2|
| bluegreen upgrade master | --deploy_type=bg_upgrade --target=master |
| bluegreen upgrade node | --deploy_type=bg_upgrade --target=node --operate=deploy --ocp_version=3.6 --new_cluster_color=green --tag=35-1012  |
| bluegreen warmup node | --deploy_type=bg_upgrade --target=node --operate=warmup  --ocp_version=3.6 --new_cluster_color=green --tag=35-1012  |
| deploy metrics  | --deploy_type=metrics --operate=deploy |
| undeploy metrics| --deploy_type=metrics --operate=undeploy |
| upgrade metrics | --deploy_type=metrics --operate=upgrade --ocp_version=3.6 |
| deploy logging  | --deploy_type=logging --operate=deploy |
| undeploy logging| --deploy_type=logging --operate=undeploy |
| upgrade logging | --deploy_type=logging --operate=upgrade --ocp_version=3.6 |
### Command Syntax

>$Commom_Command $Sub_Command

```
deploy.py --deploy_type=ocp --operate=deploy
```

