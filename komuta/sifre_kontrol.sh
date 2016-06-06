#kullanim: sifre_kontrol.sh kullanici sifre

username=$1
password=$2
salt=$(sudo getent shadow $username | cut -d$ -f3)
epassword=$(sudo getent shadow $username | cut -d: -f2)
match=$(python2 -c 'import crypt; print crypt.crypt("'"${password}"'", 
"$6$'${salt}'")')
if [ $match == $epassword ] 
then
	echo 'olumlu' 
else
	echo 'olumsuz'
fi
