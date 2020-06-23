import urllib.request
import urllib.parse
import re
import sqlite3

conn=sqlite3.connect("Proba18.db")
c=conn.cursor()


meseci=['october','november','december','january','february','march','april']

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS Proba18(datum TEXT, naziv  TEXT, gost TEXT, domacin TEXT)')

def dynamic_data_entry(i):
	if int(mesecc)<8:
		datum=eachP[10:12]+"."+mesecc+".2020"
	else:
		datum=eachP[10:12]+"."+mesecc+".2019"
	naziv=eachP[0:3] + " VS " + eachP[13:]
	domacin=eachP[13:]
	gost=eachP[0:3]
	
	c.execute("INSERT INTO Proba18 (datum,naziv,gost,domacin) VALUES (?,?,?,?)", (datum,naziv,gost,domacin))
	conn.commit()

def pokazi(domacin):
	c.execute("SELECT datum,naziv,gost,domacin FROM Proba18 WHERE domacin=?",(domacin,))
	for row in c.fetchall():
		print(row)

def ucitaj_podatke(danas):
	
	global eachP
	global mesecc

	c.execute("DELETE FROM Proba18")
	for i in range(0,len(meseci)):
		if 3>i>=0:
			mesecc=str(i+10)
		else :
			mesecc=str(i-2)
		url='https://www.basketball-reference.com/leagues/NBA_2020_games-'+meseci[i]+'.html'
		values={'s':'basics', 'submit':'search'}
		data=urllib.parse.urlencode(values)
		data=data.encode('utf-8')
		req=urllib.request.Request(url,data)
		resp=urllib.request.urlopen(req)
		respData=resp.read()
		if int(mesecc)>8:
			for datum in range(1,32):
				if datum>9:
					paragraf=re.findall(r'[A-Z][A-Z][A-Z].2019'+mesecc+str(datum)+'0[A-Z][A-Z][A-Z]', str(respData))
				else:
					paragraf=re.findall(r'[A-Z][A-Z][A-Z].2019'+mesecc+'0'+str(datum)+'0[A-Z][A-Z][A-Z]', str(respData))
				brojac1=1
				for eachP in paragraf:
					if  brojac1%2==0:
						brojac1+=1
						continue
					brojac1+=1
					dynamic_data_entry(i)
		else:
			for datum in range(1,32):
				if datum>9:
					paragraf=re.findall(r'[A-Z][A-Z][A-Z].20200'+mesecc+str(datum)+'0[A-Z][A-Z][A-Z]', str(respData))
				else:
					paragraf=re.findall(r'[A-Z][A-Z][A-Z].20200'+mesecc+'0'+str(datum)+'0[A-Z][A-Z][A-Z]', str(respData))
				brojac1=1
				for eachP in paragraf:
					if  brojac1%2==0:
						brojac1+=1
						continue
					brojac1+=1
					dynamic_data_entry(i)



