Blue Green Upgrade
-----------------

There are several ways to upgrade Ocp cluster. This ansible script provide the Blue Green Upgrade way.

*Demo Environment:*
- Architecture: 3 x Masters, 3 x Infras, 2 x App 
- New Target Cluster Color: green

*Pre-requisites*
- [Deploy OpenShift cluster](./deploy-ocp-cluster.md)

## Steps ##
1. Upgrade Master/ETCD
2. Create Green Infra/App Node
3. Registry and Router Canary Deployments
4. Update DNS or Load Balancer for Router
5. Warming the Green Nodes
   1. Disable the blue nodes 
   2. Set the green app nodes to schedulable 
   3. Update the default image streams and templates
      1. Update the packages that provide the example JSON files.
      2. Get the latest templates 
      3. Install atomic-openshift-utils and its dependencies to install the new content
      4. Update the templates ( Some errors are expected.)
   4. Import latest images
       1. In order to update your S2I-based applications, you must manually trigger a new build of those applications after importing the new images using oc start-build <app-name>.
  
6. Evacuating and Decommissioning Blue Nodes
   1. Make Green nodes scheduable
   2. Filter out masters.
   3. Evacuate pods in blue nodes
   4. Check Green node. If no issue occured, delete blue nodes. If it happens, it will roll back to blue node.


## Detail Steps: ##

### Upgrade Master/ETCD ###

```
deploy.py --deploy_type=bg_upgrade --operate=master --target=master --ocp_version=3.6
```

### Create Green Infra/App Node ###

```
deploy.py --deploy_type=bg_upgrade --operate=node --target=node --ocp_version=3.6
```

### Verifying Green Nodes
```
oc get node --show-labels -l color=green

oc adm diagnostics
```


### Registry and Router Canary Deployments ###

On one of masters, execute these commands to scale out router/registery and all pods will run on green node.

```
for node in $(oc get node -l color=green,role=infra) do ; oc adm manage-node ${node} --scheduable=true; done

oc scale dc/router --replicas=6 -n default 
oc scale dc/docker-registry --replicas=6 -n default 
```

### Update DNS or Load Balancer for Router ###
Depending on what product you are using, this step can be different. Here, DNSMASQ is the Load Balancer and it has some limitation for round robin of wildcard entries. So, one of green infra node will be added to prior to blue infra node.
```
vi /etc/dnsmasq.d/ocp-35-1012.conf

address=/masters-35-1012.gsslab.rdu2.redhat.com/10.10.181.95
address=/masters-35-1012.gsslab.rdu2.redhat.com/10.10.181.127
address=/masters-35-1012.gsslab.rdu2.redhat.com/10.10.182.4
....................NEW GREEN INFRA NODE.....................
address=/cloudapps-35-1012.gsslab.rdu2.redhat.com/10.10.182.92
address=/cloudapps-35-1012.gsslab.rdu2.redhat.com/10.10.181.21
address=/cloudapps-35-1012.gsslab.rdu2.redhat.com/10.10.182.137

```


### Warming the Green Nodes ###
```
./deploy.py --deploy_type=bg_upgrade --operate=warmup --target=node --new_cluster_color=green --ocp_version=3.6 --tag=35-1012
```

### Evacuate Pods from old cluster###
At one time, it is possible to evacuate all pods on blue nodes but it is not good idea because it makes a lot of load.
Therefore, it is recommended to evaucate pods node by node.

On master:
```
for node in $(oc get node -l color=green,role=app) do ; oc adm manage-node ${node} --scheduable=true; done

oc get node -l color=blue,type=node

NAME                                 STATUS                     AGE       VERSION
dhcp181-21.gsslab.rdu2.redhat.com    Ready,SchedulingDisabled   4d        v1.5.2+43a9be4
dhcp181-53.gsslab.rdu2.redhat.com    Ready,SchedulingDisabled   4d        v1.5.2+43a9be4
dhcp182-137.gsslab.rdu2.redhat.com   Ready,SchedulingDisabled   4d        v1.5.2+43a9be4
dhcp182-59.gsslab.rdu2.redhat.com    Ready,SchedulingDisabled   4d        v1.5.2+43a9be4
dhcp182-92.gsslab.rdu2.redhat.com    Ready,SchedulingDisabled   4d        v1.5.2+43a9be4

oadm manage-node $NODE_NAME --evacuate
```
### Delete Blue Nodes ###
```
oc delete node --selector=color=blue
```

### If something happen, Rollback to Blue ###
```
$ oadm manage-node --selector=color=green --evacuate
```

## After Work ##
Still, there are some tasks to finish upgrade. 

*Tasks*
- Delete RHEV Tag for Blue Node
- Metric Upgrade
- Logging Upgrade
- Rebuild Docker Image that use S2I image
