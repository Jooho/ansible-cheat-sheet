Ansible Playbook: Generate Self Signed Certificate
=========

This playbook help run to Jooho.generate-self-signed-cert role. 

It will create following combinations:

Case 1:
- ROOT CA
- Intermediate CA
- Server Cert (with SAN/without SAN)

Case 2:
- Root CA
- Server Cert (with SAN/without SAN)


Requirements
------------
None

Dependencies
------------

- [Jooho.generate-self-signed-cert](https://galaxy.ansible.com/Jooho/generate-self-signed-cert/)

Roles Variables
--------------
| Name                      | Default value                         |        Requird       | Description                                                                 |
|---------------------------|---------------------------------------|----------------------|-----------------------------------------------------------------------------|
| cert_base_dir             | /root/cert_base                       |         no           | Default Cert Base Directory                                                 |
| root_cert_bit             | 4096                                  |         no           | Default Root Cert Bit Size                                                  |
| intermediate_cert_bit     | 4096                                  |         no           | Default Intermediate Cert Bit Size                                          |
| server_cert_bit           | 2048                                  |         no           | Default Server Cert Bit Size                                                |
| serial_number             | 1000                                  |         no           | Cert Common Info - Serial Number                                            |
| countryName               | CA                                    |         no           | Cert Common Info - Country Name                                             |
| stateOrProvinceName       | ON                                    |         no           | Cert Common Info - Province Name                                            |
| localityName              | MILTON                                |         no           | Cert Common Info - Locality Name                                            |
| organizationName          | RED HAT                               |         no           | Cert Common Info - Org Name                                                 |
| organizationalUnitName    | SCE                                   |         no           | Cert Common Info - Org Unit Name                                            |
| emailAddress              | test@test.com                         |         no           | Cert Common Info - Email Address                                            |
| root_commonName           | Root CA                               |         no           | Root Cert Info - Root CN                                                    |
| intermediate_commonName   | Intermediate CA                       |         no           | Intermediate Cert Info - Intermediate CN                                    |
| cert_commonName           | lb.example.com                        |         no           | Server Cert Info - Server Cert CN                                           |
| use_intermediate_cert     | yes                                   |         no           | If no, it does not issue intermediate cert                                  |
| use_san                   | yes                                   |         no           | If yes, SAN info will be added with CN name                                 |
| san_dns                   |                                       |         no           | Add several SAN DNS List                                                    |
| san_ip                    |                                       |         no           | Add several SAN IP List                                                     |
| overwrite_server_cert     | yes                                   |         no           | Delete server cert directory that is based on CN name                       |
| clean_all                 | no                                    |         no           | Recreate all certs                                                          |


Example Execute Command
-----------------------

- Download roles
~~~
ansible-galaxy install -f -r requirements.yaml
~~~

- Case 1 : Intermediate certI
~~~
ansible-playbook ./playbook.yaml -e cert_commonName=kibana.cloudapps.example.com -e cert_base_dir=/home/jooho/cert_base -b -e '{san_dns: [{ index: 1, dns: "kibana-ops.cloudapps.example.com" }]}' -vvvv
~~~

- Case 2: No Intermediate cert
~~~
ansible-playbook ./playbook.yaml -e use_intermediate_cert=false -e cert_commonName=kibana.cloudapps.example.com -e cert_base_dir=/home/jooho/cert_base -b -e '{san_dns: [{ index: 1, dns: "kinaba-ops.cloudapps.example.com" }]}' -vvvv
~~~


License
-------

BSD/MIT

Author Information
------------------

This role was created in 2017 by [Jooho Lee](http://github.com/jooho).

