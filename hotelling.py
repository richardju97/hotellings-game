
# hotelling.py
# main code for hotelling's game visualization

# base example
population = 90
numspaces = 9

spaces = [0] * numspaces

custnum = 0
while custnum < population:
	spaces[custnum % numspaces] += 1
	custnum += 1
	
shop1 = 0
shop2 = 4

shop1cust = 0
shop2cust = 0

for i in range(0, numspaces):
	dist1 = abs(i - shop1)
	dist2 = abs(i - shop2)
	
	if dist1 < dist2:
		shop1cust += spaces[i]
	elif dist2 > dist1:
		shop2cust += spaces[i]
	else:
		shop1cust += (spaces[i] / 2)
		shop2cust += (spaces[i] / 2)

print("Shop 1 had " + str(shop1cust) + " Customers")
print("Shop 2 had " + str(shop2cust) + " Customers")
