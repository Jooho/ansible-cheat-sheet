How to load credential information for ansible?
-----------------------------------------------

Using plain text for password is not a good idea and sharing the information is also not a good idea.

Only special group, person who has permission know the credential information but memorizing the password is almost impossible because there are many credential information. That's why the information is usually sotred in database or encryption product. However, to use the information as an ansible variable, we need to do something different ways.

- Ansible Vault
- Enviroment Variable


## Ansible Vault 

This feature encrypt a file that contains confidential information and it is decrypted when playbook is being executed. 

**Usage:**

*Default commands*
```
ansible-vault create secret.yml
ansible-vault edit secret.yml
ansible-vault rekey secret.yml
ansible-vault encrypt secret1.yml secret2.yml
ansible-vault view secret1.yml
ansible-vault decrypt secret1.yml --output=secret1-decrypted.yml
```

*Usage with ansible playbook*
```
ansible-playbook site.yml
ansible-playbook --ask-vault-pass site.yml

echo redhat > vault-pass
chmod 600 vault-pass
ansible-playbook --vault-password-file=vault-pass site.yml ($ANSIBLE_VAULT_PASSWORD_FILE environment variable.)

ssh -o PreferredAuthentications=password ansible@servera.lab.example.com
```

*For speeding up to use Vault operations*
```
 sudo yum install python-cryptography
```

*In order to encrypt plain password*
```
password: "{{ item.pw | password_hash('sha512') }}"
```

**Demo Script**

- Using var file
```
# Create vault pass file
$ openssl rand -base64 2048 > ansible-vault.pass

# Create vault file
$ ansible-vault create a_password_file --vault-password-file=ansible-vault.pass 
password: 1234

# View encrypted value of password
$ cat a_password_file
$ANSIBLE_VAULT;1.1;AES256
37383163393732653933663065393466643865333363323831333165623830313966366663373565
6633656166323438373837373966623034616166346439300a643230633665656233323963303236
34343666653863653663653132623732396535393134613965396639383137616536626564343336
3364643264623834660a346534323631643935656339396433353332326235383032643031316333
6262

# Use the variable in ansible
$ ansible localhost -m debug -a "var=password" --vault-password-file=ansible-vault.pass -e @a_password_file    
localhost | SUCCESS => {
    "password": 1234
}

# Without password file, it shows error
$ ansible localhost -m debug -a "var=password" -e @a_password_file
ERROR! Attempting to decrypt but no vault secrets found
```

- Using encrypted string in yaml
```
# Create encrypt string
$ ansible-vault encrypt_string --vault-id ansible-vault.pass '123412' --name 'the_secret'
the_secret: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          65613565623764316139386566323462343162613762633066623638366638346434613636353035
          6561393639366238336132393831356537366334643739630a373638653738333333386561623263
          66643336623134386335386164643165386130376433623938326231366262313339383266303138
          3965646234303665350a613833666463623162313134656161396438323763383939393638353737
          3837

# Create test playbook
$ vi test.yaml
- hosts: localhost
  vars:
    the_secret: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          65613565623764316139386566323462343162613762633066623638366638346434613636353035
          6561393639366238336132393831356537366334643739630a373638653738333333386561623263
          66643336623134386335386164643165386130376433623938326231366262313339383266303138
          3965646234303665350a613833666463623162313134656161396438323763383939393638353737
          3837

  tasks:
    - debug: var=the_secret

# Use the encrypted string in ansible playbook
$ ansible-playbook -i /etc/ansible/hosts --vault-password-file=ansible-vault.pass  test.yaml  

PLAY [localhost] 
...
TASK [debug] 
********
ok: [localhost] => {
    "the_secret": "123412"
}
...
```

Tip: If you use both ways together, encrypted variable is priority.
```
$ ansible-playbook -i /etc/ansible/hosts --vault-password-file=ansible-vault.pass  test.yaml  -e @a_password_file
.. 
 TASK [debug] ******************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "the_secret": "123412"
}

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






