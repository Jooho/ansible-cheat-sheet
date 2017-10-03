Ansible Controller VM
---------------------

Ansible Controller VM need to install essential packages and also need to copy some mouldes that is not included in atomic-openshift-utils pkg.

As for ansible controller VM, Openshift subscription is nessassary so first, you need to register system with the subscription.


```



yum install -y python gcc libxml2-devel python-devel sshpass atomic-openshift-utils

git clone git clone https://github.com/ansible/ansible.git

wget https://bootstrap.pypa.io/get-pip.py

python get-pip.py



# for fedora 24 or centos7
sudo yum install -y http://resources.ovirt.org/pub/yum-repo/ovirt-release41.rpm

sudo yum config-manager --set-enabled ovirt-4.1   

sudo yum install -y python-ovirt-engine-sdk4 or  dnf install python3-ovirt-engine-sdk4


#The other
sudo pip install ovirt-engine-sdk-python 
