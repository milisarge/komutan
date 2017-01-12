//Bu yönergeyi takip ederek herhangi bir linux ortamından milis xfce4 isosunu oluşturabilirsiniz.

//Gerekli Paketler:lzip,squashfs-tools(mksquashfs),syslinux-utils(isohybrid),genisoimage

//milis klonlanır ve dizine girilir.

git clone https://github.com/milisarge/malfs-milis && cd malfs-milis

//milis-boostrap indirilir ve mnt altına lfs dizini olarak açılır.

rm -r /mnt/lfs

cd /mnt && wget http://milis.gungre.ch/iso/milis-bootstrap2016-04-21.sfs && 

unsquashfs milis-bootstrap2016-04-21.sfs && mv squashfs-root lfs && cd -

//chroot içine girilir.

./lfs-mekanizma -cg

//yukarıdaki komuttan sonra işlemler chroot içinde olacak!

mps -Ggit

//paket sunucuyu ayarlayın /root/bin/mps içinde "sunucu="

mps -G

mps -kuruld /root/talimatname/temel-ek/derleme.sira

mps -kur xorg

mps -kur xfce4

mps -kurul /root/ayarlar/gerekli_programlar

cp /root/ayarlar/.xinitrc.xfce4 /root/.xinitrc

//initrd yapmak için

cd /root

./lfs-mekanizma -bo

//paket-deposunu ve /tmp temizlemek için

rm -r /depo/paketler/*

rm -r /tmp/*

//mevcut sistem koruma noktası oluşturmak için

mps -tro

exit

// yukarıdaki komut ile chroot dışına çıkılıp iso yapılır.

//aşağıdaki iki komut ile iso yapılır.

./lfs-mekanizma -so

./lfs-mekanizma -io

//test etmek için

./qemu.sh

//not: giriş için kullanıcı:root şifre:milis
