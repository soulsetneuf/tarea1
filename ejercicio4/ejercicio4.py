def ValorCadena(cadena1,cadena2):
	if len(cadena1)>len(cadena2):
		print(cadena1)
	if len(cadena1)<len(cadena2):
		print(cadena2)
	if len(cadena1)==len(cadena2):
		print cadena1+cadena2

cadena1=raw_input()
cadena2=raw_input()
ValorCadena(cadena1,cadena2)



