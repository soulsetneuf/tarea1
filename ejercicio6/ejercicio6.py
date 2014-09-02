#coding: utf8 
def calcular_letras_numeros(frase):
	letras=0
	numeros=0
	#for x in frase: recorre caracter por caracter la cadena
	for x in frase:
		#isalpha determina si una cadena es una letra entre A-Z a-z
		if x.isalpha():
			letras=letras+1
		#isdigit determina si una cadena es un digito entre 1-9
		if x.isdigit():
			numeros=numeros+1
	print(str(letras)+" "+str(numeros))

cadena=raw_input()
calcular_letras_numeros(cadena)