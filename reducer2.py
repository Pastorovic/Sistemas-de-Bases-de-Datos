#!/usr/bin/env python

import sys

for line in sys.stdin:
	# Elimina los saltos de linea que se encuentran al final y crea una lista con sus elementos definidos por las cadenas que se encuentran entre tabuladores
	line=line.strip().split( '\t' )
	# Para cada elemento ed la lista creada se convierte su valor en tipo de coma flotante
	for i in range( 0, len( line ) ):
		line[i]=float( line[i] )
# Se imprime el valor maximo de la lista
print max( line )
