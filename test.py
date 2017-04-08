#!/usr/bin/python2
# -*- coding: utf-8 -*-
from mps import *
from arge import *
import tempfile
import filecmp
import subprocess
'''
temp = tempfile.mktemp()
def komutCalistir(c):
	out = subprocess.check_output(c,stderr=subprocess.STDOUT,shell=True,universal_newlines=True)
	return out.replace("\b","")  #encode byte format to string, ugly hack 
#arger=Arge()
gitdosyalar=[]
dosyalar=komutCalistir("ls -d  $PWD/rehber/depolar/*/*")
rehdosyalar=komutCalistir("find  $PWD/rehber/*  -maxdepth 1 -type f")
rehdosyalar=rehdosyalar.split("\n")
rehdosyalar=filter(None,rehdosyalar)
dosyalar=dosyalar.split("\n")
dosyalar=filter(None,dosyalar)
rapor=""
for dosya in dosyalar:
	for rehdosya in rehdosyalar:
		sonuc=filecmp.cmp(dosya,rehdosya)
		sonuc=str(sonuc)
		rapor+=dosya+"---"+rehdosya+"  "+sonuc+"\n"
		print(rapor)
'''
arger=Arge()
arger.gitdepo_dosyalar()
