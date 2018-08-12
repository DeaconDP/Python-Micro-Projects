""" 
My simple grid layout code

def printaRow() :
	x = 0
	while x < 5 :
		print('0',end=" ")
		x += 1

def printaCol() :
	y = 0
	while y < 8 :
		printaRow()
		print('.')
		y += 1
		
printaCol() 
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']] 

def gridLoad():
	y = 0
	x = 0
	
	
	"""
	while x < len(grid[x]) : 
		newgrid[x,y] = grid[y,x]
	"""
	"""
	while y < len(grid):
		y += 1
	"""
	
	
	
	while y < len(grid):
		while x < len(grid[x]) : 
			x += 1
			print(str(grid[x,y]),end='')
		#newgrid[i] = grid[i]
		y += 1
		x = 0
		print(y)
	
	
	
gridLoad()