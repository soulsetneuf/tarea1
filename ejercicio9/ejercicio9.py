def es_primo(numero):
	if numero==2:
	    return True
	for x in xrange(2,numero):
		if numero%x==0:
		   return False
	return True

def suma_primos(n):
	x=2
	suma=0
	ct=1
	while ct<=n:
		if es_primo(x):
			suma=suma+x
			ct=ct+1
		x=x+1
	print(suma)

n= int(raw_input())
suma_primos(n)



