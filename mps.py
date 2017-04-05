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
from arge import *
import tempfile

arger=Arge()

class Mps:
	
	def paket_sunucu(self):
		ayarlar=self.mpsayarlar()
		return ayarlar["sunucu"]
		
	def paket_kur(self,paket):
		rapor=""
		raporgc = tempfile.mktemp()
		komut="mps kur "+paket+" &> "+raporgc
		arger.komutCalistir(komut)
		with open(raporgc) as f:
			icerik = f.readlines()
		rapor+="<html>"
		for veri in icerik:
			if "cekiliyor" in veri:
				veri1=veri.split("33m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
			if "paket sunucuda yok" in veri:
				veri1=veri.split("31m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
			if "indiriliyor" in veri:
				veri1=veri.split("34m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
			if "paketi kuruldu" in veri:
				veri1=veri.split("34m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
			if "paketi kuruluyor" in veri:
				veri1=veri.split("34m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
		rapor+="</html>"
		os.remove(raporgc)
		return rapor
		
	def paket_sil(self,paket):
		rapor=""
		raporgc = tempfile.mktemp()
		komut="mps -sz "+paket+" &> "+raporgc
		arger.komutCalistir(komut)
		with open(raporgc) as f:
			icerik = f.readlines()
		rapor+="<html>"
		for veri in icerik:
			if "31m" in veri:
				veri1=veri.split("31m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
			if "32m" in veri:
				veri1=veri.split("32m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
			if "34m" in veri:
				veri1=veri.split("34m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
		rapor+="</html>"
		os.remove(raporgc)
		return rapor
	
	def paket_guncelle(self,paket):
		rapor=""
		raporgc = tempfile.mktemp()
		komut="mps -g "+paket+" &> "+raporgc
		arger.komutCalistir(komut)
		with open(raporgc) as f:
			icerik = f.readlines()
		rapor+="<html>"
		for veri in icerik:
			if "31m" in veri:
				veri1=veri.split("31m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
			if "32m" in veri:
				veri1=veri.split("32m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
			if "33m" in veri:
				veri1=veri.split("33m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
			if "34m" in veri:
				veri1=veri.split("34m")[1]
				veri2=veri1.split("[0;39m")[0]
				rapor+=veri2+"<br>"
		rapor+="</html>"
		os.remove(raporgc)
		return rapor
		
	def paketvt_guncelle(self):
		durum="olumsuz"
		raporgc = tempfile.mktemp()
		os.system("mps -G &> "+raporgc)
		rapor=open(raporgc,"r").read()
		if "güncelleniyor" in rapor:
			durum="tamam"
		return durum
		
	def git_guncelle(self):
		durum="olumsuz"
		raporgc = tempfile.mktemp()
		os.system("mps -GG &> "+raporgc)
		rapor=open(raporgc,"r").read()
		if "tamam." in rapor:
			durum="tamam"
		return durum
		
	def mpsayarlar(self,dosya="/etc/mps.conf"):
		ayarlar = {}
		with open(dosya) as ayardos:
			for satir in ayardos:
				anahtar, deger = satir.partition("=")[::2]
				ayarlar[anahtar.strip()] = deger.rstrip()
		return ayarlar
