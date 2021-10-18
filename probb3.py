def prob3():
    
    idx_0 = [11,22]
    idx_1 = [33,44]
    
    sub_1 = [idx_0, idx_1]
    sub_2 = [idx_0, idx_1]
    
    L = [sub_1, sub_2, sub_1, sub_2]
    
    return L
    
def main():
    
    ls = prob3()
    print(ls)
    
if __name__ == "__main__":
    main()