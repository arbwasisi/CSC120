"""
Author: Arsene Bwasisi
Description: This program creates a list of values from grid array
             of the diagonal elements using recursion.      
"""

def get_col(grid, n):
    """ Return list of values from column n in grid."""

    if grid == []:
        return grid
    return [grid[0][n]] + get_col(grid[1:],n-1)
    
def get_diag(grid):
    """ Return list of diagonal values in grid"""
    
    return get_col(grid,-1)

def main():
    x = [ [ 'aa', 'bb', 'cc' ],
          [ 'ee', 'ff', 'gg' ],
          [ 'kk', 'll', 'mm' ] ]
          
    diag_col = get_diag(x)
    print(diag_col)

if __name__ == "__main__":
    main()