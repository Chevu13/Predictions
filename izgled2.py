from tkinter import*
from PIL import ImageTk,Image
from dadada import*
from datetime import datetime
import glob
import re
from pravljenje_igraca_dugmeta import ispis_igrace

def citaj_podatke(danas):
	#i=IntVar()
	#broj_utakmica=0
	V=StringVar()

	c.execute("SELECT datum,naziv,gost,domacin FROM Proba18 WHERE datum=?",(danas,))
	
	
	broj_utakmica=1
	for row in c.fetchall():
		utakmicadanas=''
		utakmicadanas+=row[1]
		r1=Radiobutton(root,text=utakmicadanas,variable=V, value=utakmicadanas,indicatoron = 0,width = 20,padx = 20,command=lambda:ispis_igrace(V)).grid(row=broj_utakmica,column=1)
		for slika111 in glob.glob('C:/Users/Vuk/Desktop/kosakra/ozbiljno/aplikacija/timovi2/*.png'):
			if re.search(r'[A-Z][A-Z][A-Z]',slika111):
				imeee=re.findall(r'[A-Z][A-Z][A-Z]',slika111)
				if (imeee[0]==row[3]):
					render=ImageTk.PhotoImage(Image.open('C:/Users/Vuk/Desktop/kosakra/ozbiljno/aplikacija/timovi2/'+imeee[0]+'.png'))
					slikaa=Label(root,image=render)
					slikaa.image = render 
					slikaa.grid(row=broj_utakmica,column=2)
			if re.search(r'[A-Z][A-Z][A-Z]',slika111):
				imeee=re.findall(r'[A-Z][A-Z][A-Z]',slika111)
				if (imeee[0]==row[2]):
					render=ImageTk.PhotoImage(Image.open('C:/Users/Vuk/Desktop/kosakra/ozbiljno/aplikacija/timovi2/'+imeee[0]+'.png'))
					slikaa=Label(root,image=render)
					slikaa.image = render 
					slikaa.grid(row=broj_utakmica,column=0)
		broj_utakmica+=1
		


root=Tk()
root.title("Izgled Aplikacije")
root.iconbitmap("C:/Users/Vuk/Desktop/kosakra/ozbiljno/aplikacija/nbaa.ico")
root.geometry("400x600")
now=datetime.now()

#danas=str(now.day)+'.'+str(now.month)+'.'+str(now.year)
danas="25.12.2019"
#print(danas)
danasnjidan=Label(root,text=danas).grid(row=0,column=0)

ucitaj_podatke(1)
dugme=Button(root, text="Vidi danasnje utkamice",command=lambda:citaj_podatke(danas))
dugme.grid(row=0,column=1)


mainloop()
'''

Radiobutton(root, 
                  text=language,
                  indicatoron = 0,
                  width = 20,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)
                  '''