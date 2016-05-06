# -*- coding: utf-8 -*-

import datetime
import sys,time
import decimal

class statikrapor:
	
	col_names=[]
	stoklistvt='stoklist.db'
	html=""
	deger=0
	sirano=1
	def __init__(self):
		#self.html="<META http-equiv=content-type content=text/html;charset=windows-1254>"
		self.html=""
		self.deger=0.0
		self.data = []	
		
	def tabloekle(self):	
		#self.html+="<table border=1>"+"\n"
		self.html+="<table id='hareketrapor' border=1 class='tablesorter' ><thead>"+"\n"
	def tablobitir(self):
		self.html+="</tbody></table>"+"\n"
	def satirekle(self,noekle=0):
		if noekle==0:
			self.html+="<tr align='left'>"+"\n"
		else:
			self.html+="<tr align='left'><td>"+str(self.sirano)+"</td>"+"\n"
			self.sirano+=1
	def satirbitir(self):
		self.html+="</tr>"+"\n"
	def sutunekle(self,string):
		#string=str(string)
		#self.html+="<td><font color='blue'>"+string.decode('iso8859_9')+"</font></td>"+"\n"
		str=string.decode('latin5')
		if "href" in str  or "input" in str:
			self.html+="<td><font color='black'>"+str+"</font></td>"+"\n"
		else:
			self.html+="<td id=pano_kopya@"+str+"><font color='black'>"+str+"</font></td>"+"\n"
	def sutunac(self):
		self.html+="<td>"+"\n"
	def thsutunekle(self,string):
		self.html+="<th align='left'><font color=#003366>"+string.decode('latin5')+"</font></th>"+"\n"
	def sutunbitir(self):
		self.html+="</td>"+"\n"
	def tablo_baslik_bitir(self):
		self.html+="</thead><tbody>"+"\n"
	def tablobaslik(self,basliklar):
		self.satirekle()
		for baslik in basliklar:
			self.sutunekle(str(baslik))
		self.satirbitir()
	def linkekle(self,link,linkbas,yukle,sil):
		self.sutunekle("<a id=sisLink href="+link+">"+linkbas+"</a><p>")	
		
		if yukle!="":
			#self.sutunekle("<div id="+"yukle"+"@"+linkbas+" ><img src='static/yukle.jpeg' alt=''></div><p>")
			self.sutunekle("<input type='image' src='back16.png' name='"+yukle+"@"+linkbas+"' id='"+yukle+"@"+linkbas+"' value='<--' style='margin-left:5px;margin-right:0px; margin-top:0px;' />")
		if sil!="":
			#self.sutunekle("<div id="+"sil"+"@"+linkbas+" >sil</div><p>")
			self.sutunekle("<input type='image' src='delete16.png' name='"+sil+"@"+linkbas+"' id='"+sil+"@"+linkbas+"' value='X' style='margin-left:5px;margin-right:0px; margin-top:0px;' />")
		
		#16:38 26.10.2014 kapandi
		#self.sutunekle("<a href="+link+">"+linkbas+"</a><p>")	
		#self.divekle("deneme",linkbas)
	
	def getHtml(self):
		return self.html
		#return "<html><div id='printableArea'>"+self.html+"</div></html>"
	def getdosHtml(self,dosya):
		self.html=""
		with open(dosya) as f:
			content = f.readlines()
		self.tabloekle()
		for row in content:
			self.satirekle()
			hareket=row.split('@')
			for atom in hareket:
				self.sutunekle(atom)
			self.satirbitir()
		self.tablobitir()
		return "<html>"+self.html+"</html>"
	def getHrkt(self,dosya):
		hareketler=[[]]
		with open(dosya) as f:
			content = f.readlines()
		
		for row in content:
			row=row.split('@')
			hareketler.append(row)
			
		return hareketler
	def getlisteHtml(self,liste):
		#self.html=""
		self.tabloekle()
		for row in liste:
			self.satirekle()
			#self.sutunekle(row[2])#stkod
			self.sutunekle("<a href=http://192.168.1.254:5000/halis/"+row[2]+">"+row[2]+"</a>")
			self.sutunekle(row[4])#stkad
			self.sutunekle(row[54])#barkod1
			self.sutunekle(row[55])#barkod2
			self.sutunekle(row[56])#barkod3
			self.satirbitir()
		self.tablobitir()
		#return "<html>"+self.html+"</html>"	
		return self.html
	
	def getlisteHtml_test(self,liste):
		#self.html=""
		self.tabloekle()
		for row in liste:
			self.satirekle()
			self.sutunekle(str(row[0]))
			self.sutunekle(row[1])
			self.sutunekle(row[2])
			self.sutunekle(str(row[3]))
			self.sutunekle(str(row[4]))
			self.sutunekle(str(row[5]))
			self.sutunekle(str(row[6]))
			self.sutunekle(str(row[7]))
			self.sutunekle(str(row[8]))
			self.satirbitir()
		self.tablobitir()
		#return "<html>"+self.html+"</html>"	
		return self.html
	
	def diziYhtml(self,dizi,dizibas,topsut=[]):
		alttoplam=[]
		for j in range(0,len(topsut)):
			alttoplam.append(0)
		self.tabloekle()
		#self.tablobaslik(dizibas)
		for bas in dizibas:
			self.thsutunekle(bas)
		self.tablo_baslik_bitir()
		for row in dizi:
			self.satirekle()
			for i in range(0,len(row)):
				deger=row[i]
				if(type(deger) is int or type(deger) is float or type(deger) is decimal.Decimal):	
					if i in topsut:
						alttoplam[i]+=deger
				self.sutunekle(str(deger))
			self.satirbitir()
		#alttoplam ekleme	
		self.satirekle()
		for i in range(0,len(dizibas)):
			if i in topsut:
				self.sutunekle(str(alttoplam[i]))
			else:
				self.sutunekle('-')
		self.satirbitir()
		self.tablobitir()
		return self.html
	
	def diziYhtml2(self,dizi,dizibas,topsut=[]):
		alttoplam=[]
		for j in range(0,len(topsut)):
			alttoplam.append(0)
		self.tabloekle()
		#self.tablobaslik(dizibas)
		for bas in dizibas:
			self.thsutunekle(bas)
		self.tablo_baslik_bitir()
		for degerx in dizi:
			
			self.satirekle()
			for deger in degerx.split():
				if(type(deger) is int or type(deger) is float or type(deger) is decimal.Decimal):	
					if i in topsut:
						alttoplam[i]+=deger
				self.sutunekle(str(deger))
			self.satirbitir()
		#alttoplam ekleme	
		self.satirekle()
		for i in range(0,len(dizibas)):
			if i in topsut:
				self.sutunekle(str(alttoplam[i]))
			else:
				self.sutunekle('-')
		self.satirbitir()
		self.tablobitir()
		return self.html
	
	def calistir(self,sql):
		sqlparca=""
		con=""
		try:
			con = mdb.connect(baglanti.host, baglanti.kullanici,baglanti.sifre,baglanti.vt)
			con.set_character_set('latin5')
			cur = con.cursor()
			#print "htmlrapor.py-baglanti acildi"
			sql=sql.split(';')
			for sqlparca in sql:
				cur.execute(sqlparca)
				rows = cur.fetchall()
				if(rows):
					self.col_names = [i[0] for i in cur.description]
					#print col_names
					rows=list(rows)
					if con:    
						#print "htmlrapor.py-baglanti kapandi-select islemi"
						con.close()	
					return rows	
			if con:    
				print "htmlrapor.py-baglanti kapandi-select islemi"
				con.close()	
			
		except :
			print "htmlrapor.py-HATA:",str(sys.exc_info()[1])
			if con:    
				#print "htmlrapor.py-baglanti kapandi-select islemi"
				con.close()
