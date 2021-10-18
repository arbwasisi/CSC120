"""
Author: Arsene Bwasisi
Description: This program takes in a list l, and uses recursion
			 to swap even and odd indexes with each other.      
"""

def xchg(l):
	"""Returns a list where the odd and even indexes are swapped."""
    
	if len(l) == 1 or len(l) == 0:
		return l
        
	l[0], l[1] = l[1], l[0]
	return l[:2] + xchg(l[2:])

def main():
    
    print(xchg([1, 2, 3, 4, 5, 6, 7] ))

if __name__ == "__main__":
    main()