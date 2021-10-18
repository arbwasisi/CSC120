# Author: Arsene Bwasisi
# Description: This program uses the jaccard index calculation to
#              determine the similarities of two sets.
#              

def jaccard(set1, set2):
    """
    Function divides length of intersection of set1 and 2 by
    lenght of union of set1 and 2 to get the similarity value.
    """

    intersection = set1.intersection(set2)
    union = set1.union(set2)
    
    # if both ests are empty return 1
    if len(intersection) == 0 and len(union) == 0:
    	return 1/1
    else:
    	jaccard_index = len(intersection)/len(union)
    	return jaccard_index
    
def main():
    
    set1 = set(input(''))
    set2 = set(input(''))  
    jaccard(set1, set2)
    
if __name__ == "__main__":
    main()
    