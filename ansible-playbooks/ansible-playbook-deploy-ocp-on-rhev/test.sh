ansible-playbook playbooks/config.yaml  -M  /root/ansible/lib/ansible/modules/packaging/os/  -vv --forks=12 -i /etc/ansible/hosts   -e @vars/all -i a.yaml -e deploy_type=ocp_deploy
ansible-playbook /usr/share/ansible/openshift-ansible/playbooks/byo/config.yml --fork=12  -i /etc/ansible/hosts

