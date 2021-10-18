"""
Author: Arsene Bwasisi
Description: This program creates a list of values from grid array
             of the diagonal elements(top-right to bottom-left)
             using recursion.      
"""


def get_diag2(grid):
    """ Return list of diagonal values in a grid."""
    
    if grid == []:
        return grid

    return [grid[0][len(grid)-1]] + get_diag2(grid[1:])
        
def main():
    
    x = [ [ 'aa', 'bb', 'cc' ],
          [ 'ee', 'ff', 'gg' ],
          [ 'kk', 'll', 'mm' ] ]
          
    diag_col = get_diag2(x)
    print(diag_col)

if __name__ == "__main__":
    main()