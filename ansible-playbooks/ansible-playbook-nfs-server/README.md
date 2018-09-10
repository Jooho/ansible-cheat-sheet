Setup NFS Server
----------------

## 1. Download ansible galaxy role
ansible-galaxy install -f -r requirements.yaml -p ./roles

## 2. Update variable
```
vi vars/all

nfs_server_ip: infra_node
nfs_mount_point: /exports
nfs_block_dev_name: sdc
```

## 3. Execute ansible
```
ansible-playbook -i /etc/ansible/hosts playbook.yaml -e @vars/main.yml
```

