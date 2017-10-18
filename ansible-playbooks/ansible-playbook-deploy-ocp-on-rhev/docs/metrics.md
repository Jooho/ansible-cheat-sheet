Metrics Component
---------------------------

*Features*
- Deploy
- Undeploy
- Upgrade

### Deploy Metrics During OCP Installation ####

Edit vars/ocp_param then install OCP cluster.
```
# Metrics
openshift_hosted_metrics_deploy: true

```

### Deploy Metrics After OCP Installation ###
```
./deploy.py --deploy_type=metrics --operate=deploy
```

### Undeploy Metrics ###

```
./deploy.py --deploy_type=metrics --operate=undeploy
```


### Upgrade Metrics ###

```
./deploy.py --deploy_type=metrics --operate=upgrade --ocp_version=3.6
```
