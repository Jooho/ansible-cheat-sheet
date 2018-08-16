How to load credential information for ansible?
-----------------------------------------------

Using plain text for password is not a good idea and sharing the information is also not a good idea.

Only special group, person who has permission know the credential information but memorizing the password is almost impossible because there are many credential information. That's why the information is usually sotred in database or encryption product. However, to use the information as an ansible variable, we need to do something different ways.

- Ansible Vault
- Enviroment Variable


## Ansible Vault 

This feature encrypt a file that contains confidential information and it is decrypted when playbook is being executed. 

Usage:

Default commands
```
ansible-vault create secret.yml
ansible-vault edit secret.yml
ansible-vault rekey secret.yml
ansible-vault encrypt secret1.yml secret2.yml
ansible-vault view secret1.yml
ansible-vault decrypt secret1.yml --output=secret1-decrypted.yml
```

Usage with ansible playbook
```
ansible-playbook site.yml
ansible-playbook --ask-vault-pass site.yml

echo redhat > vault-pass
chmod 600 vault-pass
ansible-playbook --vault-password-file=vault-pass site.yml ($ANSIBLE_VAULT_PASSWORD_FILE environment variable.)

ssh -o PreferredAuthentications=password ansible@servera.lab.example.com
```

For speeding up to use Vault operations
```
 sudo yum install python-cryptography
```

In order to encrypt plain password
```
password: "{{ item.pw | password_hash('sha512') }}"
```



## Environment Variable

This uses linux environment variables with 600 file permission that only allow an owner to read and write the file. 


### Create a file that contains sensitive information & export the variables.

```
$ vi ~/.source
export JKIT_ID=jooho
export JKIT_PW=test123


$ chmod 600 ~/.source
-rw------- 1 jooho jooho 30 Aug 16 09:52 /home/jooho/.source

$ source ~/.source

$ env|egrep "^JKIT_ID=|^JKIT_PW=" 

JKIT_ID=jooho
JKIT_PW=test123
```

### How to use Environment variables in Ansible
```
$ vi vars/main.yml

id: "{{lookup('env', 'JKIT_ID')}}"
pw: "{{lookup('env', 'JKIT_PW')}}" 
```






