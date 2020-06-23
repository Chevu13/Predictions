import re
from tkinter import*
from PIL import Image, ImageTk
import urllib.request
import urllib.parse
import re
import sqlite3
from urllib.request import urlopen
import requests
from ucitavanjestatistike import igracstats



'''
for slika in glob.glob('C:/Users/Vuk/Desktop/kosakra/ozbiljno/aplikacija/timovi/*.png'):
	img_ime=Image.open(slika).filename
	img_ime=img_ime[::-1]
	img_ime=img_ime[4:7]
	img_ime=img_ime[::-1]
	print(img_ime)
	'''




def ispis_igrace(V):

	K=StringVar()

	top=Toplevel()
	top.title("Izabrana Utakmica")
	top.iconbitmap("C:/Users/Vuk/Desktop/kosakra/ozbiljno/aplikacija/nbaa.ico")

	utakmica=V.get()
	print(utakmica)

	gost=utakmica[0:3]
	domacin=utakmica[7:]

	im = Image.open('C:/Users/Vuk/Desktop/kosakra/ozbiljno/aplikacija/timovi2/'+gost+'.png')
	render=ImageTk.PhotoImage(im)
	slikaa=Label(top,image=render)
	slikaa.image = render 
	slikaa.grid(row=0,column=1)
	im2 = Image.open('C:/Users/Vuk/Desktop/kosakra/ozbiljno/aplikacija/timovi2/'+domacin+'.png')
	render1=ImageTk.PhotoImage(im2)
	slikaa1=Label(top,image=render1)
	slikaa1.image = render1 
	slikaa1.grid(row=0,column=2)

	broj_utakmica=0
	url='https://www.basketball-reference.com/teams/'+gost+'/2020.html'
	requests.get(url)
	values={'s':'basics', 'submit':'search'}
	data=urllib.parse.urlencode(values)
	data=data.encode('utf-8')
	req=urllib.request.Request(url,data)
	resp=urllib.request.urlopen(req)
	respData=resp.read()
	imena_gostujuce_ekipe=[]
	imena_domace_ekipe=[]
	for i in range(0,5):
		igracihtml=re.findall(r'<tr ><th scope="row" class="center " data-stat="ranker" csk="." >.<\/th><td class="left " data-append-csv=".+?".+?csk=".+?>.+?>[A-Z].+?<', str(respData))
		#print(igracihtml[i])
		paragraf=igracihtml[i][::-1]
		pravoime=''
		for i in range(1,40):
			if paragraf[i] =="\\":
				continue
			if paragraf[i] == ">":
				break
			pravoime+=paragraf[i]
		pravoime=pravoime[::-1]
		print(pravoime)
		imena_gostujuce_ekipe.append(pravoime)
	#print(imena_gostujuce_ekipe)
	for i in range(len(imena_gostujuce_ekipe)):
		r2=Radiobutton(top,text=imena_gostujuce_ekipe[i],variable=K, value=imena_gostujuce_ekipe[i]+"?"+domacin,indicatoron = 0,command=lambda:igracstats(K),width = 20,padx = 20).grid(row=broj_utakmica+1,column=1)
		broj_utakmica+=1

	




	broj_utakmica=0
	url1='https://www.basketball-reference.com/teams/'+domacin+'/2020.html'
	requests.get(url1)
	values1={'s':'basics', 'submit':'search'}
	data1=urllib.parse.urlencode(values1)
	data1=data1.encode('utf-8')
	req1=urllib.request.Request(url1,data1)
	resp1=urllib.request.urlopen(req1)
	respData1=resp1.read()
	for i in range(0,5):
		igracihtml=re.findall(r'<tr ><th scope="row" class="center " data-stat="ranker" csk="." >.<\/th><td class="left " data-append-csv=".+?".+?csk=".+?>.+?>[A-Z].+?<', str(respData1))
		#print(igracihtml[i])
		paragraf=igracihtml[i][::-1]
		pravoime=''
		for i in range(1,40):
			if paragraf[i] =="\\":
				continue
			if paragraf[i] == ">":
				break
			pravoime+=paragraf[i]
		pravoime=pravoime[::-1]
		print(pravoime) 
		imena_domace_ekipe.append(pravoime)
	#print(imena_domace_ekipe)

	for i in range(len(imena_domace_ekipe)):
		r2=Radiobutton(top,text=imena_domace_ekipe[i],variable=K, value=imena_domace_ekipe[i]+"?"+gost,indicatoron = 0,command=lambda:igracstats(K),width = 20,padx = 20).grid(row=broj_utakmica+1,column=2)
		broj_utakmica+=1