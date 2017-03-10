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

class Arge:
	
	def runShellCommand(self,c):
		out = subprocess.check_output(c,stderr=subprocess.STDOUT,shell=True,universal_newlines=True)
		return out.replace("\b","")  #encode byte format to string, ugly hack 
	
	def dizin_cek(self,dizin='dizin',uzanti=""):
		#dizinyol='/'+dizin
		flst=[]
		lst=os.listdir(dizin)
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
		
	def kurulum_oku(self,kurulumdos):
		with open("kurulum/"+kurulumdos, 'r') as f:
			param = yaml.load(f)
		return param

	def kurulum_yaz(self,param,kurulumdos):
		with open("kurulum/"+kurulumdos, 'w') as outfile:
			yaml.dump(param, outfile, default_flow_style=False)
