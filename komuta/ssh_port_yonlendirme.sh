#ssh sunucudaki hizmete erisim
ssh -L 9000:localhost:5432 user@example.com
#yerelden ssh a hizmet sunma
ssh -R 9000:localhost:3000 user@example.com
