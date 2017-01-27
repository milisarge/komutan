#ssh-keygen -t rsa
publickey_yol=~/.ssh/id_rsa.pub
cat $publickey_yol | ssh user@hostname 'cat >> .ssh/authorized_keys'
