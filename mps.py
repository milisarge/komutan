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
		arger.komutCalistir("mps kur "+paket+" &> "+raporgc)
		with open(raporgc) as f:
			icerik = f.readlines()
		rapor+="<html>"
		for veri in icerik:
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
