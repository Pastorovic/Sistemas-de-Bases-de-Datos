#!/usr/bin/env python

import sys

for line in sys.stdin:
	# Se divide cada linea en eelementos que se encuentran entre tabuladores
	fields=line.split('\t')
	# Si la linea contiene 26 elementos se procesa la linea
	if len(fields) == 26:
		# Se escogen los 13 primeros campos y se le incluyen los campos de max, min y avg iniciados a 0.0
		fields=fields[0:13]+['0.0', '0.0', '0.0']
		# Se recorre la linea y se imprimen todos sus elementos separados por un tabulador
		for field in fields:
			# Se imprime cada campo seguido de una tabulacion
			print '%s\t' % field,
		# Se imprime un salto de linea
		print '\n',
