# -*- coding: utf-8 -*-
import sqlite3 as sqlmak
import sys
import datetime
import os
import decimal
import time
import codecs
import random
import re
import sys
import urllib2, urllib
from random import randint
import datetime
from stdnum import ean
import ctypes
import codecs
import subprocess
import crypt
import yaml
import hashlib
import filecmp

class Arge:
	
	def komutCalistir(self,c):
		out = subprocess.check_output(c,stderr=subprocess.STDOUT,shell=True,universal_newlines=True)
		return out.replace("\b","")  #encode byte format to string, ugly hack 
		
	def dizin_cek(self,dizin='dizin',uzanti=""):
		#dizinyol='/'+dizin
		flst=[]
		lst=os.listdir(dizin)
		lst=[x for x in lst if os.path.isfile((dizin+"/"+x))]
		if uzanti=="":
			return sorted(lst)
		else:
			for dosya in lst:
				if dosya.endswith("."+uzanti):
					flst.append(dosya)
			return sorted(flst)
	
	def komut_kos(self,komut,onkomut=""):
		
		komut=komut.strip()
		komckt="kondarma/"+str(randint(0,1000))+".ckt"
		komkos=komckt+".kos"
		if onkomut=="":
			onkomut="bash "
		codecs.open(komkos,"w","utf-8").write(komut)
		tumkomut=onkomut+" "+komkos+" 2>"+komckt
		
		process = subprocess.Popen(tumkomut,stdout=subprocess.PIPE,shell=True)
		proc_stdout = process.communicate()[0].strip()
		hsonuc=codecs.open(komckt,"r").read()
		os.system("rm "+komkos)
		os.system("rm "+komckt)
		return proc_stdout+"<p>"+"---"+"<p>"+hsonuc+"</p>"

	def komut_doskos(self,komutdos):
		komut=""
		komut=codecs.open("komuta/"+komutdos,"r").read()
		return self.komut_kos(komut)
	
	def param_al(self,komutdos):
		paramlar={}
		komut=codecs.open("komuta/"+komutdos,"r",'utf-8').read()
		komut=komut.split("\n")
		for kom in komut:
			if '=' in kom and 'if' not in kom:
				baslik=kom.split('=')[0]
				deger=kom.split('=')[1]
				paramlar[baslik]=deger
		return paramlar
	
	def param_guncelle(self,mevcut,guncel):
		for baslik in mevcut:
			mevcut[baslik]=guncel[baslik]
		return mevcut
	
	
	def calistir(self,sql):
		con = sqlmak.connect("sql/bilbet.db")
		cur = con.cursor()
		cur.execute(sql)
		data=cur.fetchall()
		return data
		con.close()
		
	def calis(self,sql):
		con = sqlmak.connect("sql/bilbet.db")
		cur = con.cursor()
		cur.execute(sql)
		con.commit()
		con.close()
	
	def hesap_ekle(self,posta,isim,sifre):
		con = sqlmak.connect("sql/bilbet.db")
		cur = con.cursor()
		cur.execute("INSERT INTO hesap (posta,isim,sifre) VALUES (?,?,?)", (posta,isim,sifre))
		con.commit()
		con.close()
	
	def hesap_dogrula(self,isim,gelen_sifre):
		con = sqlmak.connect("sql/bilbet.db")
		cur = con.cursor()
		cur.execute("select sifre from hesap where isim='"+isim+"'")
		sifre=cur.fetchall()[0][0]
		print sifre
		if sifre==gelen_sifre:
			return 1
		else:
			return 0
		con.close()
	
	def girdi_kontrol(self,no):
		sql=open('./sql/girdi_kontrol.sql','r').read()
		sql=sql.replace('@no@',str(no))
		row=self.calistir(sql)
		if (row):
			if row[0][0]=='e':
				return 1
		return None
	
	def girdi_ekle(self,isim):
		print isim
		if self.girdi_kontrol(isim) is None:
			sql=open('./sql/girdi_ekle.sql','r').read()
			sql=sql.replace('@isim@',str(isim))
			print "sql:",sql
			print self.calis(sql)
	
	def girdi_sil(self,no):
		sql=open('./sql/girdi_sil.sql','r').read()
		sql=sql.replace('@no@',str(no))
		return self.calis(sql)
		
	def girdi_no(self,isim,sifre):
		sql=open('./sql/girdi_no.sql','r').read()
		sql=sql.replace('@isim@',str(isim))
		sql=sql.replace('@sifre@',str(sifre))
		row=self.calistir(sql)
		if (row):
			return row[0][0]
		return None
		
	def sifre_kontrol(self,isim,sifre):
		saltkom="sudo getent shadow "+isim+" | cut -d$ -f3"
		process = subprocess.Popen(saltkom,stdout=subprocess.PIPE,shell=True)
		salt = process.communicate()[0].strip()
		epasskom="sudo getent shadow "+isim+" | cut -d: -f2"
		process = subprocess.Popen(epasskom,stdout=subprocess.PIPE,shell=True)
		epass = process.communicate()[0].strip()
		match=crypt.crypt(sifre,"$6$"+salt)
		if match==epass:
			return 1
		else:
			return 0
		
	def coklu_topla(self,miktar):
		if '+' in str(miktar):
			miktarlar=miktar.split('+')
			topmik=0
			for mik in miktarlar:
				if mik.find(",") > 0 :
					mik=mik.replace(',','.')
				mik=float(mik)
				topmik+=mik
			miktar=topmik
			miktar=str(miktar)
		if '*' in str(miktar):
			miktarlar=miktar.split('*')
			topmik=1
			for mik in miktarlar:
				if mik.find(",") > 0 :
					mik=mik.replace(',','.')
				mik=float(mik)
				topmik*=mik
			miktar=topmik
			miktar=str(miktar)
		if '/' in str(miktar):
			miktarlar=miktar.split('/')
			bolnn=miktarlar[0]
			bol=miktarlar[1]
			if bolnn.find(",") > 0 :
				bolnn=bolnn.replace(',','.')
			if bol.find(",") > 0 :
				bol=bol.replace(',','.')
			miktar=float(bolnn)/float(bol)
		else:
			return miktar
		return str(round(float(miktar),3))
		
	def saat_al(self):	
		saatstr=""
		now = datetime.datetime.now()
		saatstr=now.strftime("%H:%M:%S")
		return saatstr
		
	def dosyaYdizi(self,dosya):
		icerik=codecs.open(dosya, "r","latin5")
		stoklar=[]
		for satir in icerik:
			sat=satir.split("\n")[0]
			sat=sat.split("\r")[0]
			stoklar.append([sat])
		return stoklar
		
	def servisler_al(self,dosya="servisler.ayar"):
		icerik=codecs.open(dosya, "r","latin5")
		servisler=[]
		for satir in icerik:
			sat=satir.split("\n")[0]
			sat=sat.split("\r")[0]
			servisler.append(sat)
		return servisler
	
	def link_kontrol(self,link):
		indirme_komut="curl -s "
		sonuc=self.komutCalistir(indirme_komut+link)
		if "Not Found" in sonuc:
			return False
		else:
			return True
	
	def gitdepo_dosyalar(self):
		gitdosyalar=[]
		dosyalar=self.komutCalistir("find  $PWD/rehber/depolar/*/  -maxdepth 1 -type f")
		rehdosyalar=self.komutCalistir("find  $PWD/rehber/*  -maxdepth 1 -type f")
		rehdosyalar=rehdosyalar.split("\n")
		rehdosyalar=filter(None,rehdosyalar)
		dosyalar=dosyalar.split("\n")
		dosyalar=filter(None,dosyalar)
		rapor=""
		for dosya in dosyalar:
			sonuc=True
			for rehdosya in rehdosyalar:
				sonuc=filecmp.cmp(dosya,rehdosya)
				if sonuc:
					break
			if sonuc is False:
				dosya=dosya.split("depolar/")[1]
				gitdosyalar.append(dosya)
		#open("/tmp/rapor","w").write(rapor)
		return gitdosyalar
	def gitdepo_ekle(self,link):
		if self.link_kontrol(link):
			depoyer="rehber/depolar/"
			sonuc="" 
			hesap="" 
			depo=""
			hesdep=""
			depo_ekle_komut="git clone "
			if "github.com" in link:
				hesdep=link.split("github.com/")[1]
				sonuc=hesdep
				hesap=hesdep.split("/")[0]
				depo=hesdep.split("/")[1]
				hesdep=hesap+"-"+depo
			depo_ekle_komut+=link+" "
			if hesap != "" and depo != "":
				if os.path.exists(depoyer+hesdep):
					return "depo zaten var!"
				else:
					depo_ekle_komut+=depoyer+hesdep
			else:
				return "hesap veya depo belirsizliği!"
			print depo_ekle_komut
			sonuc=self.komutCalistir(depo_ekle_komut)
			return sonuc
		else:
			return "kırık link!"
		
	def kurulum_oku(self,kurulumdos):
		with open("kurulum/"+kurulumdos, 'r') as f:
			param = yaml.load(f)
		return param

	def kurulum_yaz(self,param,kurulumdos):
		with open("kurulum/"+kurulumdos, 'w') as outfile:
			yaml.dump(param, outfile, default_flow_style=False)
	
	def diskler(self,tip="ext4"):
		diskler=[]
		komut="blkid | grep "+tip+" | awk '$1 !~ /live/ {print $1}' | sed s'/.$//'"
		veriler=self.komutCalistir(komut).split("\n")
		diskler=filter(None,veriler)
		return diskler
		
	def bolumFormatla(self,hedef):
		komut="umount -l "+hedef
		if os.path.exists(hedef):
			os.system(komut)
			komut2="mkfs.ext4 -F " + hedef
			try:
				os.system(komut2)
				print hedef,"formatlandı."
				return True
			except OSError as e:
				time.sleep(1)
				return "hata=formatlanamadi!"
		else:
			time.sleep(1)
			return "hata=disk bolumu yok!"

	def takasAyarla(self,bolum):
		try:
			os.system("mkswap "+"/dev/"+bolum)
			os.system('echo "`lsblk -ln -o UUID /dev/' + bolum + '` none swap sw 0 0" | tee -a /etc/fstab')
			return True
		except OSError as e:
			time.sleep(1)
			return "hata:takas islemi!"
			
	def bolumBagla(self,hedef,baglam):
		komut="mount "+hedef+" "+baglam
		try:
			os.system(komut)
			return True
		except OSError as e:
			time.sleep(1)
			return "hata:bolum baglanamadi!"
			
	def kullaniciOlustur(self,isim,kullisim,kullsifre):
		try:
			os.system("kopar milislinux-"+isim+" "+kullisim)
			os.system('echo -e "'+kullsifre+'\n'+kullsifre+'" | passwd '+kullisim)
			#masaustu ve diğer ayarların aktarılması
			ayar_komut="cp -r /root/.config /home/"+kullisim+"/"
			os.system(ayar_komut)
			saat_komut="saat_ayarla_tr"
			os.system(saat_komut)
			print "kullanıcı işlemleri yapıldı."
			return True
		except OSError as e:
			time.sleep(1)
			return "hata:kullanici islemleri!"
			
	def sistemOlustur(self,baglam):
		komut=""
		try:
			#bazı dizinleri atlamak için ve hız rsync
			yenidizinler=["srv","proc","tmp","mnt","sys","run","dev","media"]
			for ydizin in yenidizinler:
				komut="mkdir -p "+baglam+"/"+ydizin
				os.system(komut)
			print "yenidizinler oluşturuldu."
			return True
		except OSError as e:
			time.sleep(1)
			return "hata:yeni dizinler olusturma!"
	
	def dizinKopyala(self,kaynak,hedef):
		komut="rsync --delete -a /"+kaynak+" "+hedef+" --exclude /proc"
		try:	
			os.system(komut)
			print kaynak,"kopyalandı."
			return True
		except OSError as e:
			time.sleep(1)
			return "hata:"+kaynak+" dizin kopyalanmasi!"
		
	def initrdOlustur(self,hedef):
		try:
			if hedef != "":
				os.system("mount --bind /dev "+hedef+"/dev")
				os.system("mount --bind /sys "+hedef+"/sys")
				os.system("mount --bind /proc "+hedef+"/proc")
				os.system('chroot '+hedef+' dracut --no-hostonly --add-drivers "ahci" -f /boot/initramfs')
				print "intird kuruldu."
				return True
			else:
				return "hata:initrd baglami tanimsiz!"
		except OSError as e:
			time.sleep(1)
			return "hata:initrd olusturulamadi!"

	def grubKur(self,hedef,baglam):
		hedef = hedef[:-1]
		if hedef == "/dev/mmcblk0": #SD kart'a kurulum fix
			os.system("grub-install --boot-directory="+baglam+"/boot /dev/mmcblk0")
		else:
			os.system("grub-install --boot-directory="+baglam+"/boot " + hedef)
		os.system("chroot "+baglam+" grub-mkconfig -o /boot/grub/grub.cfg")
		print "grub kuruldu."
		return True

	def bolumCoz(self,hedef):
		komut="umount -l "+hedef
		try:
			os.system(komut)
			print hedef,"çözüldü."
			return True
		except OSError as e:
			time.sleep(1)
			return "hata:Bolum cozulemedi!"

