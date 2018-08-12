#vars
inventory = {'rope':1, 'torch':0, 'gold':10, 'dagger':0}


#funcs
def displayInventory():
	
	print('Inventory:')
	i = 0
	total = 0
	
	for k, v in inventory.items():
		print(k + ": " + str(v))
		total += v
	
	print('total stuff: ' + str(total))

	
def addToInventory(booty):
	for b in booty:
		if b in inventory.keys():
			inventory[b] += 1
		else:
			inventory.setdefault(b,1)
	#if 'gold coin' in booty:
	#	inventory.gold += 1
		
	

#calls
displayInventory()
addToInventory(['gold', 'dagger', 'ruby'])
displayInventory()