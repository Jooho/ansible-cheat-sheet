Base RHEL Image 
---------------

There are several ways to deploy rhel vm in RHEV but this doc does not explain about it. It only provide that what preparation are needed for the base image.


### Storage for docker ###
- For root (20G)
- For docker (30G)

**Example:**
```
Size: 30
Alias: docker
Interface: VirtIO
Allocation Policy: Thin Provision
```

### RedHat Subscription Manager Register ###

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

### New User and Configure sudoers ###
*jooho is example user so you can change it*

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
