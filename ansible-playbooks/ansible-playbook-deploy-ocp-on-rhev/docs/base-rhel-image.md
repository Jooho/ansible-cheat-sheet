Base RHEL Image 
---------------

There are several ways to deploy rhel vm in RHEV but this doc does not explain how to create it. It will only provide which preparation needs.


### Attach storage for docker ###
```
Size: 30
Alias: docker
Interface: VirtIO
Allocation Policy: Thin Provision
```

### Register Right RHSM Pool ###

```
subscription-manager register --username=XXXX  --password=XXXX
subscription-manager attach --pool=XXXX
```

### Enable/Install Necessary Repos and Packages ###
```
subscription-manager repos --disable="*"
yum-config-manager --disable \*
subscription-manager repos \
    --enable="rhel-7-server-rpms" \
    --enable="rhel-7-server-extras-rpms" \
    --enable rhel-7-server-rh-common-rpms

yum repolist

yum install -y wget git net-tools bind-utils iptables-services bridge-utils bash-completion kexec-tools sos psacct  rhevm-guest-agent-common 

yum update

# To get fqdn, ovirt-guest-agent should be installed
systemctl enable ovirt-guest-agent
systemctl start ovirt-guest-agent
```

### Add a new user and add it to sudoers ###
*jooho is just example user*

```
useradd jooho
echo "jooho ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
```

### Sealing a Linux Virtual Machine ###
```
touch /.unconfigured
rm -rf /etc/ssh/ssh_host_*
echo "HOSTNAME=localhost.localdomain" >  /etc/sysconfig/network 
rm -rf /etc/udev/rules.d/70-*
subscription-manager clean
```

#### Network Script ####
*Edit /etc/sysconfig/network-scripts/ifcfg-eth0*
```
TYPE="Ethernet"
BOOTPROTO="dhcp"
NAME="eth0"
DEVICE="eth0"
ONBOOT="yes"
PEERDNS=no
```

**Reference**
- [Sealing a Linux Virtual Machine](https://www.ovirt.org/documentation/vmm-guide/chap-Templates/)
