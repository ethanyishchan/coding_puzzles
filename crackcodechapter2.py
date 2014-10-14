class Address:
	def __init__(self, number, street, country):
		self.number = number
		self.street = street
		self.country = country


	def prettyPrint(self):
		print self.number, self.street, self.country

	def printCountry(self):
		print self.country


x = Address ("148C", "Lorong Kismis", "Singapore")
Address.prettyPrint(x) 	
Address.printCountry(x)