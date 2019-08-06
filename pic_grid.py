#! python3

"""You can think of grid[x][y] as being the character 
at the x- and y-coordinates of a “picture” drawn with 
text characters. The (0, 0) origin will be in the 
upper-left corner, the x-coordinates increase going right,
and the y-coordinates increase going down."""

def pic_grid(a):
	for item in grid:
		for i in item:
			print(i, end=' ')
		print('\n')
			
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

pic_grid(grid)
