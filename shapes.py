def shape_alpha():
    
    return [[10,'abc','jkl',40],[[1.1,-17],[123,456]]]
    
def shape_bravo():
    
    array = [[['whoa','excellent'],['bogus','righteous']],[[],'rufus']]
    array[1][0] = array[0][1]
    
    return array
    
def shape_charlie(arg1):
    
    return [[[[None,arg1],arg1],arg1],arg1]
    
def shape_delta(arg1,arg2):
    
    return [arg1,arg2,[arg1,[arg1,arg2,[arg1,arg2],[30]],[20],arg2],[10]]
    
def shape_echo(arg1,arg2,arg3):
    
    array = [[[[],arg3],arg2],arg1]
    array[0][0][0] = array
    
    return array
    
def main():
    
    shape_alpha()
    shape_bravo()
    
if __name__ == "__main__":
    main()
    