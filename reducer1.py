#!/usr/bin/env python

import sys

for line in sys.stdin:
	# Elimina los saltos de linea que se encuentran al final y crea una lista con sus elementos definidos por las cadenas que se encuentran entre tabuladores
	fields=line.strip().split('\t')
	# Se crea una lista vacia
	gs=[]
	# Se recorren los campos gsm19023, gsd19024, gsd19025 y gsd19026
	for field in fields[2:6]:
		# Si el valor de dicho campo es la cadena 'null' se le asigna el valor ASCII 0x00, que simboliza el valor null
		if field == 'null':
			fields[fields.index(field)]=0X00
		# En otro caso se introduce el valor en la lista creada
		else:
			gs.append(float(field))
	# Se imprimen los 13 primeros campos, seguido cada uno de ellos por un tabulador
	for field in fields[0:13]:
		print '%s\t'% field,
	# A partir de la lista creada se imprimen los 3 ultimos campos, separados por tabuladores, calculando el maximo, minimo y avg de la lista
	print '%s\t%s\t%s\n'% (max(gs), min(gs), sum(gs)/len(gs)),
