inicio = int(raw_input())
fin = int(raw_input())
lista=[]
lista2=[]
for x in xrange(inicio,fin+1):
	lista.append(x)
print lista
for x in lista:
	if x%2==0:
		lista2.append(x)
print lista2
