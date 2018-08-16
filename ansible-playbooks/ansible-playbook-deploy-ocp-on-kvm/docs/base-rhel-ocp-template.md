Create OCP RHEL Template
------------------------

When Base RHEL VM is ready, ocp_rhel_template should be created based on the vm.
You can create template using rhev webconsole or use ansible. Following ansible script help create RHEV temaplate from vm.

```
- hosts: localhost
  tasks: 
    - name: Create RHEV Template
      ovirt_templates:
        auth:
          username: "{{rhev.id}}"
          password: "{{rhev.pw}}"
          url: "{{rhev.api_url}}"
          ca_file: "{{rhev.ca_file}}"
        cluster: Default
        name: RHEL_7U3_for_OCP
        vm: jlee_RHEL_7U3_BASE_for_OCP
        cpu_profile: Test
        description: Test
```
