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

arger=Arge()

class Mps:
	
	def paket_sunucu(self):
		ayarlar=self.mpsayarlar()
		return ayarlar["sunucu"]
		
	def paketvt_guncelle(self):
		durum="olumsuz"
		os.system("mps -G &> /tmp/mpsG.log")
		rapor=open("/tmp/mpsG.log","r").read()
		if "güncelleniyor" in rapor:
			durum="tamam"
		return durum
		
	def git_guncelle(self):
		durum="olumsuz"
		os.system("mps -GG &> /tmp/mpsGit.log")
		rapor=open("/tmp/mpsGit.log","r").read()
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
