//temel iso yapmak(minimal iso)

cd /sources/milis.git

mkdir -p /mnt/lfs

export LFS=/mnt/lfs

./lfs-mekanizma -ia

agdan_sirali_kur /root/talimatname/temel/derleme.sira /mnt/lfs/

agdan_sirali_kur /root/talimatname/temel-ek/derleme.sira /mnt/lfs/

./lfs-mekanizma -cg

//yukarıdaki komuttan sonra işlemler chroot içinde olacak!

cd /tmp

rm *.PRE

for i in *.POST; do bash "$i"; done

//sorunsuz calisirsa kur-kos betikleri

rm *.POST

//initrd yapmak için

cd /root

./lfs-mekanizma -bo

exit 

// yukarıdaki komut ile dışarı çıkılıp iso yapılır.

./lfs-mekanizma -so

./lfs-mekanizma -io

./qemu.sh
