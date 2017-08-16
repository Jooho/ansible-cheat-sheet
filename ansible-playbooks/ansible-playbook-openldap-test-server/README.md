Ansible Playbook: OpenLDAP Test Server
=========

This playbook contains Jooho.generate-self-signed-cert and Jooho.openldap-test-server
It can generate certificate and apply it for the OpenLDAP server. Moreover it will put some data for test purpose.


Requirements
------------
None

Dependencies
------------

- [Jooho.generate-self-signed-cert](https://galaxy.ansible.com/Jooho/generate-self-signed-cert/)
- [Jooho.openldap-test-server](https://galaxy.ansible.com/Jooho/openldap-test-server/)

Roles Variables
--------------

| Name                      | Default value                         |        Requird       | Description                                                                 |
|---------------------------|---------------------------------------|----------------------|-----------------------------------------------------------------------------|
| ssl                       |  true                                 |         no           | Enable SSL for LDAP Server                                                  |
|                           |                                       |                      | Generate cert/cacert/private key                                            |
| use_intermediate_cert     |  false                                |         no           | If set true, it will create Root + Intermediate + Server cert (Refer [Jooho.generate-self-signed-cert](https://galaxy.ansible.com/Jooho/generate-self-signed-cert/) |
| cert_commonName           |  ldap.example.com                     |         no           | Hostname for ldap server ssl certificate                                    |
| cert_base_dir             |  /root/cert_base                      |         no           | Base certificate folder                                                     |


Example Execute Command
-----------------------

- Download roles
```
ansible-galaxy install -f -r requirements.yaml
```

- Non SSL LDAP Server
```
ansible-playbook ./playbook.yaml -b
```

- SSL LDAP Server with Intermediate Cert
```
ansible-playbook ./playbook.yaml -b -e ssl=true -e use_intermediate_cert=true -e cert_commonName=ldap.example.com -e cert_base_dir=/home/jooho/cert_base/ldap -e '{san_ip: [{ index: 0, dns: "192.168.200.110" }]}'
```

- SSL LDAP Server with Root Cert
```
ansible-playbook ./playbook.yaml -b -e ssl=true -e cert_commonName=che.example.com -e cert_base_dir=/home/jooho/cert_base/ldap -e '{san_ip: [{ index: 0, dns: "192.168.200.110" }]}'
```

Client Configuration
--------------------
The root-ca.cert.pem file will be found on ldap server vm

```
TLS_CACERTDIR /etc/openldap/cacerts
TLS_CACERT    /etc/openldap/certs/root-ca.cert.pem
TLS_REQCERT allow
```

Useful Commands
----------
```

ldapadd -x -w redhat -D "cn=read-only-admin,dc=example,dc=com" -f base.ldif

ldapsearch -v -H ldaps://ldap.example.com -D "cn=read-only-admin,dc=example,dc=com" -w "redhat" -b "dc=example,dc=com" -o ldif-wrap=no   -vvvv

ldapmodify -h ldap.example.com -p 389 -D "cn=read-only-admin,dc=example,dc=com" -f user-passwd.ldif -w redhat

ldapdelete -H ldaps://ldap.example.com -D "cn=read-only-admin,dc=example,dc=com" "cn=Sue Jacobs,ou=People,dc=example,dc=com" -w redhat -vvv

```

License
-------

BSD/MIT

Author Information
------------------

This role was created in 2017 by [Jooho Lee](http://github.com/jooho).

