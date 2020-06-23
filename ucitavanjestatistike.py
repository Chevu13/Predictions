import urllib.request
import urllib.parse
import re
import sqlite3
from urllib.request import urlopen
import requests
from poslednje import projekcija


def igracstats(K):
	Podatak=K.get()
	Podaci=Podatak.split("?")
	ime_igraca=Podaci[0]
	tim=Podaci[1]
	if ime_igraca=='Nikola Jokixc4x87':
		ime_igraca='Nikola Jokic'
	if ime_igraca=='Luka Donxc4x8ixc4x87':
		ime_igraca='Luka Doncic'
	if ime_igraca=='Kristaps Porzixc5x862x4xa3is':
		ime_igraca='Kristaps Porzingis'
	if ime_igraca=='Dxc4x81vis Bertxc4x81ns':
		ime_igraca='Davis Bertans'
	if ime_igraca=='Nikola Vuxc4x8devixc4x87':
		ime_igraca='Nikola Vucevic'
	if ime_igraca=='Bojan Bogdanovixc4x87':
		ime_igraca='Bojan Bogdanovic'
	if ime_igraca=='Bogdan Bogdanovixc4x87':
		ime_igraca='Bogdan Bogdanovic'
	if ime_igraca=='Goran Dragixc4x87':
		ime_igraca=='Goran Dragic'
	print(ime_igraca)
	print(tim)
	projekcija(ime_igraca,tim)



