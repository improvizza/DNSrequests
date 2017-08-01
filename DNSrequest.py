#!/user/bin/python
# -*- coding: utf-8 -*-

import dns
import dns.resolver
import dns.query
import dns.zone
from ipwhois import IPWhois
from pprint import pprint
import socket

dominios=[]
que=0
def salir(): exit()
def atras(): print "..Volviendo"
def gestorErrores(): print "La opción introducida no es correcta!!!\n"
def archivo():ruta = raw_input('Introduce el nombre del archivo (debe estar en la misma carpeta): ')
def manual():
	cuantos = raw_input('Cuantos dominios quieres introducir? ')
	for i in range(0,int(cuantos)):
		dominios.append(raw_input('Introduce dominio: '))	
def resolverDNS():
	for i in dominios:
		respuestas = dns.resolver.query(i, 'MX')
		print "***********************************************"
		print "Los DNS del dominio "+i+" son:\n"
		for rdata in respuestas:
			print rdata.exchange
	print "***********************************************"
	print "Listo!"
def queip():
	for i in dominios:
		print "La ip de "+i+" es "+socket.gethostbyname(i)
	print "Listo!"
def quienes():
	for i in dominios:
		print "La respuesta del whois en el dominio "+i+" es: "
		ip=socket.gethostbyname(i)
		obj = IPWhois(ip)
		results = obj.lookup_rdap(depth=1)
		pprint(results)
	print "Listo!"
principal={
	"1": manual,
	"2": salir,
	}
consultas={
	"1": queip,
	"2": resolverDNS,
	"3": quienes,
	"4": atras,
	}
print "\nBienvenido!\n\nQué quieres hacer?"
while True:
	while True:
		como = raw_input("(1)Introducir dominios manualmente\n(2)Salir\n\nIntroduce una opción: ")
		principal.get(como,gestorErrores)()
		print "\n\n...Dominios cargados! :)\n"
		que=0
		break
	while int(que) is not 4:
		que = raw_input("Ahora qué?\n(1)Ver sus IPs\n(2)Resolver DNSs\n(3)Hacer un WHOIS\n(4)Atrás\n\nIntroduce una opción: ")
		consultas.get(que,gestorErrores)()
		
