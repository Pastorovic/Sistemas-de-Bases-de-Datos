#!/usr/bin/env python

import sys

for line in sys.stdin:
	# Elimina los saltos de linea que se encuentran al final y crea una lista con sus elementos definidos por las cadenas que se encuentran entre tabuladores
	fields=line.strip().split('\t')
	# Si el campo ubicado en la tercera posicion de la lista transformado a tipo float se encuentra entre 100 y 1000
	if float(fields[2]) >= 100.0 and float(fields[2]) <= 1000.0:
		# Se imprimer el ultimo campo del array
		print '%f\t' % float(fields[15]),
