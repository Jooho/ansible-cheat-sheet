Ansible Role Development Guide
-----------------------------

0. Create Role 
```
molecule init --role $ROLE_NAME --driver=docker  
```

1. Update Molecule Configuration
```
docker:
  containers:
    - name: ansible-role-test-openldap-server
      image: centos              <==== Update
      image_version: latest
      ansible_groups:
        - group1

```

2. Decide Default Vars
~~~
temp_dir: /tmp
ldap.port: 389
ldap.hostname: ldap.example.com
~~~

3. Only List Up Flow with names on tasks/main.yaml 
~~~
 - name: Install OpenLDAP packages and necessary packages
 
 - name: Get RootPW for openLDAP

 - name: Copy db.ldif file to {{temp_dir}}

 - name: Modify ldap with db.ldif

 - name: Copy monitor.ldif to {{temp_dir}}
..
..
~~~

4. Develop one by one 
~~~
 - name: Install OpenLDAP packages and necessary packages
   package:
    name: "{{item}}"
    state: latest
   with_items:
    - openldap
    - compat-openldap
    - openldap-clients
    - openldap-servers
    - openldap-servers-sql
    - openldap-devel
~~~

5. Deploy test container
~~~
molecule test --destroy=never
~~~

6. Test each task
~~~
molecule converge
~~~

