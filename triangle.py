"""
Author: Arsene Bwasisi
Description: This program uses recursion to build riangular array
			 of size n containing val.
"""

def triangle(n, val):
	""" Return a triangular array of size n with value val."""

	if n == 0:
		return []
        
	return triangle(n-1, val) + [[val]*n]

def main():
    
    res = triangle(3, 37)
    print(res)

if __name__ == "__main__":
    main()
