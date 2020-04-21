
# hotelling.py
# main code for hotelling's game visualization

# base example
population = 90 #total number of customers on the beach
numspaces = 9 #total number of locations on the beach

# create our beach with our customers
spaces = [0] * numspaces
custnum = 0
while custnum < population:
	spaces[custnum % numspaces] += 1
	custnum += 1
	
shop1 = 0 #location of shop 1
shop2 = 4 #locaiton of shop 2

shop1cust = 0 #number of customers for shop 1
shop2cust = 0 #number of custoemrs for shop 2

for i in range(0, numspaces):
	dist1 = abs(i - shop1) #distance from this spot to shop 1
	dist2 = abs(i - shop2) #distance from this spot to shop 2
	
	# allocate customers based on whichever is closer
	if dist1 < dist2:
		shop1cust += spaces[i]
	elif dist2 > dist1:
		shop2cust += spaces[i]
	else:
		# allocate evenly if the distance is the same
		shop1cust += (spaces[i] / 2)
		shop2cust += (spaces[i] / 2)

# print results
print("Shop 1 had " + str(shop1cust) + " Customers")
print("Shop 2 had " + str(shop2cust) + " Customers")
