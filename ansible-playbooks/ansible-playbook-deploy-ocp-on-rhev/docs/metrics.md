Metrics Component
---------------------------

There are 2 ways to deploy Metrics component in this ansible script: during installion, after installation.

### Deploy Metrics ###
#### During OCP Installation ####

Edit vars/ocp_param then install OCP cluster.
```
# Logging
openshift_hosted_logging_deploy: true

```

#### After OCP Installation ####
```
./deploy.py --deploy_type=metrics --operate=deploy
```

### Undeploy Metrics ###

```
./deploy.py --deploy_type=metrics --operate=undeploy
```

