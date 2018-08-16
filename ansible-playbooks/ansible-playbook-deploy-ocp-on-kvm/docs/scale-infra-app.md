Scale up/down Infra/app Node 
----------------------------

It supports scaling up and down of infra/app nodes then, it creates RHEV VM and install OCP automatically.
Basically, it scales up only 1 vm but you can specify vm count. When you scale down, the node will try cordon/drain.

*Common Useful Options*
- instances: If set count, it will create/teardown VMs up to the count.



### Scale Up Infa/app Node ###
```
# scale up 1 infra node
./deploy.py --deploy_type=scale --operate=up --target=infra

# scale up 2 infra node
./deploy.py --deploy_type=scale --operate=up --target=infra --instances=2

# scale up 1 app node
./deploy.py --deploy_type=scale --operate=up --target=app

# scale up 2 app node
./deploy.py --deploy_type=scale --operate=up --target=app --instances=2
```

### Scale Down Infa/app Node ###
```
# scale donw 1 infra node
./deploy.py --deploy_type=scale --operate=down --target=infra

# scale down 2 infra node
./deploy.py --deploy_type=scale --operate=down --target=infra --instances=2

# scale down 1 app node
./deploy.py --deploy_type=scale --operate=down --target=app

# scale down 2 app node
./deploy.py --deploy_type=scale --operate=down --target=app --instances=2
