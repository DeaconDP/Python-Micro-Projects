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
	y = len(grid) -1
	x = 0
	i = 0	
	
	while x <= len(grid[y]) - 1:
		while y >= 0: 
			focusline = grid[y]
			print(focusline[x], end = '')
			y -= 1
		print('')
		y = len(grid) -1
		x += 1
	
gridLoad()
