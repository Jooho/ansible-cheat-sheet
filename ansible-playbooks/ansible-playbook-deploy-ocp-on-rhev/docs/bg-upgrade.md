Blue Green Upgrade
-----------------

There are several ways to upgrade Ocp cluster. This ansible script provide the Blue Green Upgrade way.

**Steps**
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
  1. Filter out masters.
  2. Evacuate pods in blue nodes
  3. Check Green node. If no issue occured, delete blue nodes. If it happens, it will roll back to blue node.



**Detail Information for each steps**

### Upgrade Master/ETCD ###

```
deploy.py --deploy_type=bg_upgrade --target=master
```

### Create Green Infra/App Node ###

```
deploy.py --deploy_type=bg_upgrade --target=node

```

### Registry and Router Canary Deployments ###

On one of masters

```
TODO - scheduable for infra green node

oc scale dc/router --replicas=6 -n default 
oc scale dc/docker-registry --replicas=6 -n default 
```

### Update DNS or Load Balancer for Router ###
Depending on what product you are using, this step can be different. Here, DNSMASQ is the Load Balancer and it has some limitation for round robin of wildcard entries. So, one of green infra node will be added to prior to blue infra node.
```

```
