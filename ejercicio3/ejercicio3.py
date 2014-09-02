def es_palindromo(cadena):
	#cadena[::-1] invierte la cadena
	if str(cadena[::-1])==cadena:
		print("True")
	else:
		print("False")

cadena=raw_input()
es_palindromo(cadena)
