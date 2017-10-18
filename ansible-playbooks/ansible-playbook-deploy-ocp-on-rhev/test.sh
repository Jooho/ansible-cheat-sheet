ansible-playbook playbooks/config.yaml  -M  ./modules  -vv --forks=12 -i /etc/ansible/hosts   -e @vars/all -i a.yaml -e deploy_type=ocp_deploy
ansible-playbook /usr/share/ansible/openshift-ansible/playbooks/byo/config.yml --fork=12  -i /etc/ansible/hosts

# ocp_cluster
# ora --provider=rhev --deploy_type=ocp_cluster  --var_file="/path/to/file"
# ansible-playbook playbooks/config.yaml  -M  ./modules  -vv --forks=12 -i /etc/ansible/hosts   -e @/path/to/file -i a.yaml -e deploy_type=ocp_cluster

# infra scaling
# ora --provider=rhev --deploy_type=app --vm_count=1 --var_file="/path/to/file"
# ansible-playbook playbooks/config.yaml  -M  ./modules  -vv --forks=12 -i /etc/ansible/hosts   -e @/path/to/file -i a.yaml -e deploy_type=infra -e new_infra_node_vms=1

# app scaling
# ora --provider=rhev --deploy_type=app --vm_count=2 --var_file="/path/to/file"
# ansible-playbook playbooks/config.yaml  -M  ./modules  -vv --forks=12 -i /etc/ansible/hosts   -e @/path/to/file -i a.yaml -e deploy_type=app -e new_app_node_vms=1

# bg_upgrade version 1
# ora --provider=rhev --deploy_type=bg_upgrade  --upgrade_version=3.5 --var_file="/path/to/file"
# ansible-playbook playbooks/config.yaml  -M  ./modules  -vv --forks=12 -i ./inventory/rhev/hosts/rhev.py   -e @vars/all -e @vars/ocp_params  -e deploy_type=bg_upgrade -e target=node 

# bg_upgrade version 2
# ora --provider=rhev --deploy_type=bg_upgrade  --upgrade_version=3.5 --var_file="/path/to/file" --tag="35-0912"
# ansible-playbook playbooks/config.yaml  -M  ./modules  -vv --forks=12 -i /etc/ansible/hosts   -e @/path/to/file -i a.yaml -e deploy_type=bg_upgrade -e new_infra_node_vms=3 -e new_app_node_vms=2 -e ocp_version=3.5


# scaledown
# ansible-playbook playbooks/config.yaml  -M  ./modules -vvvv --forks=12 -i inventory/rhev/hosts/a.py  -e @vars/all  -e deploy_type=stop -e target_vm=app  -e provider=rhev -e @vars/ocp_params 
# ansible-playbook playbooks/config.yaml  -M  ./modules -vvvv --forks=12 -i inventory/rhev/hosts/a.py  -e @vars/all  -e deploy_type=scaledown -e target_vm=infra -e provider=rhev -e @vars/ocp_params


# Teardown
#./deploy.py --deploy_type=ocp --operate=teardown --tag=35-1012 --target_node_filter=green --ocp_install=false -vvvv
