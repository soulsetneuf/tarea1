def tabla_divicion():
	#\t sirve para tabular da un espacio entre los numeros
	for x in xrange(1,11):
		for y in xrange(1,11):
			print(str(y*x)+"/"+str(y)+"="+str(y*x/y))+"\t",
		print("")

tabla_divicion()