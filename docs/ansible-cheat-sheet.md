
## Get IP from target node
```
- hosts: localhost
  tasks:
   - command: echo "{{hostvars[item]['ansible_default_ipv4']['address']}}"
     with_items:
      - "{{ groups.masters }}"
```
