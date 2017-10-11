Credential Information
---------------------
Credential information should be separated from ansible script for security reason.

Therefore, OS environment parameter is used for login/subs information. Moreover, this setup file should be controlled by administrator

**Notice: it script  must be sourced before ansible script executes.**

*setup*
```
# RHEV(upstream name: Ovirt) Information
export OVIRT_USERNAME=USER@Profile
export OVIRT_PASSWORD=
export OVIRT_URL=https://X.X.redhat.com/ovirt-engine/api
export OVIRT_CA_PATH=/root/rhev.crt


# Base Image Credential Information
export BASE_IMAGE_ID=root
export BASE_IMAGE_PW=redhat

# Red hat subscription manager information
export RHSM_ID=''
export RHSM_PW=''

# Subscription Name or Pool ID (If both set, Pool ID has more priority)
export BROKER_SUB_POOL="Red Hat OpenShift Container Platform Broker/Master Infrastructure
export NODE_SUB_POOL="Red Hat OpenShift Container Platform, Standard, 2-Core"
export BROKER_SUB_POOL_ID="XXXXXXX"
export NODE_SUB_POOL_ID="XXXXXXX"

```

**Execute following command at first before executing ansible script**
```
source ~/setup
```
