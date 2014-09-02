def secuencia(c):
	for x in range(1,c+1):
		print str(x)*x
	z=c-1
	while z>0:
		print str(z)*z
		z=z-1

c=int(raw_input())
secuencia(c)

