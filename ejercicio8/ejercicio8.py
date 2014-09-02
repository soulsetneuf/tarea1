def triangulo(l1,l2,l3):
	if teorema_pitagoras(l1,l2,l3):
		return "Rectangulo"
	if l1==l2 and l2==l3:
		return "Equilatero"
	if l1==l2 and l2!=l3:
		return "Isoseles"
	if l1!=l2 and l2==l3:
		return "Isoseles"
	if l1==l3 and l3!=l2:
		return "Isoseles"
	if l1!=l2 and l2!=l3:
		return "Escaleno"
	return "No es triangulo"
  
def teorema_pitagoras(a,b,c):
	catetos=0
	hipotenusa=0
	mayor=0
	if a>b and a>c:
		hipotenusa=a*a
		catetos=(c*c)+(b*b)
	if b>a and b>c:
		hipotenusa=b*b
		catetos=(a*a)+(c*c)
	if c>a and c>b:
		hipotenusa=c*c
		catetos=(a*a)+(b*b)
	if hipotenusa==catetos:
		return True
	else:
		return False


lado1=int(raw_input())
lado2=int(raw_input())
lado3=int(raw_input())
print triangulo(lado1,lado2,lado3)