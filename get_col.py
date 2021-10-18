"""
Author: Arsene Bwasisi
Description: This program creates a list of values from column n 
			 in a grid array using recursion.      
"""

def get_col(grid, n):
    """ Return list of values from column n in grid."""
	
    if grid == []:
        return grid
    return [grid[0][n]] + get_col(grid[1:],n)

def main():
    x = [ [ 'aa', 'bb', 'cc' ],
          [ 'ee', 'ff', 'gg' ],
          [ 'kk', 'll', 'mm' ] ]
          
    col = get_col(x,2)
    print(col)

if __name__ == "__main__":
    main()