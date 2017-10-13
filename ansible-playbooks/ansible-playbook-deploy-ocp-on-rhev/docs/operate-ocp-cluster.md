Operation - OpenShift Container Platform Cluster
-------------------------------------------

Ansible script provide the easy ways to maintains OCP cluster and RHEV VMs.
By default, before stop/teardonw, it will wait sometime for evacuate all pods on the node that will be gone.

*Features*
- start single/multiple nodes or cluster
- stop single/multiple nodes or cluster
- teardown single/multiple nodes or cluster

*Common Useful option for operations*
- tag: If there are multiple clusters, you can specify specific ocp cluster
- target_node_filter: It can specific nodes operated to.


### start single/multiple nodes or cluster

```
# start cluster
./deploy.py --deploy_type=ocp --operate=start

# start infra nodes
./deploy.py --deploy_type=ocp --operate=start --target_node_filter=infra

# start infra_1 node
./deploy.py --deploy_type=ocp --operate=start --target_node_filter=infra_1
```


### stop single/multiple nodes or cluster

```
# stop cluster
./deploy.py --deploy_type=ocp --operate=stop

# stop infra nodes
./deploy.py --deploy_type=ocp --operate=stop --target_node_filter=infra

# stop infra_1 node
./deploy.py --deploy_type=ocp --operate=stop --target_node_filter=infra_1

```


### teardown single/multiple nodes or cluster

*Useful option*
- ocp_install : If set false, it skips cordon/drain node before teardown. It makes faster teardown.

```
# teardown cluster
./deploy.py --deploy_type=ocp --operate=teardown --ocp_install=false

# teardown infra nodes
./deploy.py --deploy_type=ocp --operate=teardown --target_node_filter=infra

# teardown infra_1 node
./deploy.py --deploy_type=ocp --operate=teardown --target_node_filter=infra_1

```



