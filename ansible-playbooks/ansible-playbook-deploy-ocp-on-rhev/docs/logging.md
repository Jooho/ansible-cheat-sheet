Logging Component
---------------------------

There are 2 ways to deploy logging component in this ansible script: during installion, after installation.

### Deploy Logging ###
#### During OCP Installation ####

Edit vars/ocp_param then install OCP cluster.
```
# Logging
openshift_hosted_logging_deploy: true

```


#### After OCP Installation ####
```
./deploy.py --deploy_type=logging --operate=deploy
```

### Undeploy Logging ###
```
./deploy.py --deploy_type=logging --operate=undeploy
```
