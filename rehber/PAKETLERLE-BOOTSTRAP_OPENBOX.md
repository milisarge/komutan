//Bu yönergeyi takip ederek herhangi bir linux ortamından milis ortamını oluşturabilirsiniz.

//Gerekli Paketler:lzip,squashfs-tools(mksquashfs),syslinux-utils(isohybrid),genisoimage

//milis klonlanır ve dizine girilir.

git clone https://github.com/milisarge/malfs-milis && cd malfs-milis

//milis sisteminin kurulabilmesi için öndosyalar ve gerekli ayarlar yapılır.

./lfs-mekanizma -ia

//mps-bootstrap içindeki sunucu="ip:port/"  şeklinde paket depo adresi ayarlandıktan sonra

//paket güncellemesi yapılır 

./mps-bootstrap -G

//temel-sistem kurulumu için.

./mps-bootstrap -psk  openboxT1.pklist /mnt/lfs/

//gerekli ayarlamalar için chroot içine girilir.

./lfs-mekanizma -cg

//yukarıdaki komuttan sonra işlemler chroot içinde olacak!

cp /root/ayarlar/.xinitrc.openbox /root/.xinitrc

cd /tmp

rm *.PRE

//DİKKAT!!! 2 KERE ÇALIŞTIRILACAK

for i in *.POST; do bash "$i"; done

for i in *.POST; do bash "$i"; done

//sorunsuz calisirsa kur-kos betikleri silinebilir.

rm *.POST

bash /root/talimatname/genel/openbox/openbox.kur-kos

cp -R /etc/xdg/openbox/ /root/.config/  

obmenu-generator -s -i

//initrd yapmak için

cd /root

./lfs-mekanizma -bo

//temel sistem için paket durum tarihçesi oluşturulur.

mps -tro

exit

// yukarıdaki komut ile chroot dışına çıkılıp iso yapılır.

//aşağıdaki iki komut ile iso yapılır.

./lfs-mekanizma -so

./lfs-mekanizma -io

//test etmek için

./qemu.sh

//not: giriş için kullanıcı:root şifre:milis
