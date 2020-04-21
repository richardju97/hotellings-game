
# hotelling.py
# main code for hotelling's game visualization

# base example w/ objects
class Hotelling:
	def __init__(self, p, n):
		self.population = p #total number of customers on the beach
		self.numspaces = n #total number of locations on the beach
		
		# create our beach with our customers
		self.createcustomers()
	
	def createcustomers(self):
		self.spaces = [0] * self.numspaces
		custnum = 0
		while custnum < self.population:
			self.spaces[custnum % self.numspaces] += 1
			custnum += 1
	
	def createshops(self, i, j):
		assert self.checkbounds(i), "Error: Shop 1 location is out of bounds"
		assert self.checkbounds(j), "Error: Shop 2 location is out of bounds"
		self.shop1 = i #location of shop 1
		self.shop2 = j #locaiton of shop 2
		self.shop1cust = 0 #number of customers for shop 1
		self.shop2cust = 0 #number of custoemrs for shop 2

	def checkbounds(self, i):
		return(i >= 0 and i < self.numspaces)

	def calculate(self):
		for i in range(0, self.numspaces):
			dist1 = abs(i - self.shop1) #distance from this spot to shop 1
			dist2 = abs(i - self.shop2) #distance from this spot to shop 2
		
			# allocate customers based on whichever is closer
			if dist1 < dist2:
				self.shop1cust += self.spaces[i]
			elif dist2 < dist1:
				self.shop2cust += self.spaces[i]
			else:
				# allocate evenly if the distance is the same
				self.shop1cust += (self.spaces[i] / 2)
				self.shop2cust += (self.spaces[i] / 2)

	def printshopcustomers(self):
		# print results
		print
		print("Shop 1 had " + str(self.shop1cust) + " Customers")
		print("Shop 2 had " + str(self.shop2cust) + " Customers")
		print

	def printconfig(self):
		#print config parameters
		print
		print("Population: " + str(self.population))
		print("Spaces: " + str(self.numspaces))
		print("Shop 1 Location: " + str(self.shop1))
		print("Shop 2 Location: " + str(self.shop2))
		print

h = Hotelling(90, 9)
h.createshops(0, 8)
h.calculate()
h.printconfig()
h.printshopcustomers()

h.createshops(0, 4)
h.calculate()
h.printconfig()
h.printshopcustomers()

h.createshops(3, 4)
h.calculate()
h.printconfig()
h.printshopcustomers()

h.createshops(4, 4)
h.calculate()
h.printconfig()
h.printshopcustomers()
