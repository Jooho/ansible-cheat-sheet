Integrated Playbooks with OpenShift Official Ansible Scripts
-------------------------------------------------------------
Sometimes, we need to create ansible script for internal OCP and we can found there are several duplicated scripts. 
If offical playbooks can execute from internal ansible playbook, it does not need to spend time developing duplicated scripts.
This doc show you how to integrate official ansible scripts with internal ansible playbook.

*Note: Some official playbooks need more prerequisite tasks to execute*

## Hosts file ##
### Dynamic Inventory Hosts File (AWS/GCE/ETC) ###
For Cloud provider, we usually use dynamic inventory hosts file, which means there is a ansible task to initialize groups. Dislike normal VM(e.g. VMWARE), the ansible script create hosts file every time.
In this case, a playbook for integrated need to include the task file( usually named generate-host-groups.yaml ).

```
- hosts: localhost
  tasks:
    - name: Initialize OCP groups based on cloud tag.
      include: "playbooks/rhev/tasks/generate-host-groups.yaml"

# For using official ansible script, these 2 scripts help initialize groups & add hosts to memory.
- include: "/usr/share/ansible/openshift-ansible/playbooks/byo/openshift-cluster/initialize_groups.yml"
- include: "/usr/share/ansible/openshift-ansible/playbooks/common/openshift-cluster/evaluate_groups.yml"
```

### Static Hosts file (VMWARE/RHEV/ETC) ###
With static hosts file, only 2 ansibles tasks are needed to initialize groups for official ansible script.

```
# For using official ansible script, these 2 scripts help initialize groups & add hosts to memory.
- include: "/usr/share/ansible/openshift-ansible/playbooks/byo/openshift-cluster/initialize_groups.yml"
- include: "/usr/share/ansible/openshift-ansible/playbooks/common/openshift-cluster/evaluate_groups.yml"
```



## Example official ansible playbook: Deploying external openshift provisioner ##
Include the playbook into a internal playbook.

```
# Include the specific script that you want to try.
- include: /usr/share/ansible/openshift-ansible/playbooks/common/openshift-cluster/openshift_provisioners.yml

```


# Full Demo 
** Create efs.yaml playbook **
```
- hosts: localhost
  tasks:
    - name: Initialize OCP groups based on cloud tag.
      include: "playbooks/rhev/tasks/generate-host-groups.yaml"

# For using official ansible script, these 2 scripts help initialize groups & add hosts to memory.
- include: "/usr/share/ansible/openshift-ansible/playbooks/byo/openshift-cluster/initialize_groups.yml"
- include: "/usr/share/ansible/openshift-ansible/playbooks/common/openshift-cluster/evaluate_groups.yml"
```

** Execute playbook**

```
ansible-playbook  -vvvv   ./efs.yaml \
-e openshift_provisioners_install_provisioners=True \
-e openshift_provisioners_efs=True \
-e openshift_provisioners_efs_fsid=fs-XXXX \
-e openshift_provisioners_efs_region=us-east-1 \
-e openshift_provisioners_efs_aws_access_key_id=XXXX \
-e openshift_provisioners_efs_aws_secret_access_key=XXXX \
-e openshift_provisioners_project=openshift-infra \
-e openshift_provisioners_efs_nodeselector='{"role"="infra"}' \
-e openshift_provisioners_image_prefix=openshift3/ \
-e openshift_provisioners_image_version=v3.6 \
-e openshift_provisioners_efs_path=/data/persistentvolumes \
-e provider=rhev -e @vars/all -e @vars/ocp_params      
```

