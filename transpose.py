"""
Author: Arsene Bwasisi
Description: This program will transform a given grid of numbers
             to where the rows become the column and vice versa.     
"""

def get_col(grid, n):
    """ Return list of values from column n in grid."""
	
    if grid == []:
        return grid
        
    return [grid[0][n]] + get_col(grid[1:],n)

def transpose(grid, n=0):
    """Returns a new grid that has been transposed."""
    
    if n == len(grid):
       return [] 
    
    col = get_col(grid, n)
    return [col] + transpose(grid, n+1)

def main():

    x = [ [ 'aa', 'bb', 'cc' ],
          [ 'ee', 'ff', 'gg' ],
          [ 'kk', 'll', 'mm' ] ]
          
    t = transpose(x)
    print(t)

if __name__ == "__main__":
    main()