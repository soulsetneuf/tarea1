class Circulo:
	radio=0
	area=0
	pi=3.1416
	def __init__(self, radio):
		self.radio=radio
	def darArea(self):
		area=(self.radio*self.radio)*self.pi
		return area

radio=int(raw_input("RADIO: "))
c=Circulo(radio)
print "AREA: "+str(c.darArea())

