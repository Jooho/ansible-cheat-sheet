# OpenShift RHEV Reference Architecture


This script help deploy OpenShift on RHEV and also provide some more features for reference


## Script Features
- setup ansible controller
- ocp cluster deploy
- ocp cluster operation(start/stop/teardown)
- scale out infra/app
- scale down infra/app
- blue green upgrade master
- blue green upgrade node operation(deploy/teardown)

## Docs
### Tested Scripts
- [Tested Features](./docs/tested_scripts.md)

### Pre-requisites
- [Download RHEV Cert](./docs/download-rhev-cert.md)
- [Parameters](./docs/parameters.md)
- [Credential Information](./docs/setup.md)
- [Create base rhel image](./docs/base-rhel-image.md)
- [Create ocp base template](./docs/base-rhel-ocp-template.md)
- [Dynamic inverntory host file](./docs/dynamic_inventory.md)

### Deploying VM/OCP/Metrics/Logging + Scale/BG Upgrade ###
- [Set up ansible controller vm](./docs/ansible-controller-vm.md)
- [Deploy OpenShift cluster](./docs/deploy-ocp-cluster.md)
- [Operate OpenShift cluster](./docs/operate-ocp-cluster.md)
- [Metrics](./docs/metrics.md)
- [Logging](./docs/logging.md)
- [Scale up/down infra/app nodes](./docs/scale-infra-app.md)
- [Blue Green Upgrade](./docs/bg-upgrade.md)
  




