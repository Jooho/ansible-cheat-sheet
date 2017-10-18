Logging Component
---------------------------


### Deploy Logging During OCP Installation ###

Edit vars/ocp_param then install OCP cluster.
```
# Logging
openshift_hosted_logging_deploy: true

```

#### Deploy Logging After OCP Installation ####
```
./deploy.py --deploy_type=logging --operate=deploy
```

### Undeploy Logging ###
```
./deploy.py --deploy_type=logging --operate=undeploy
```
