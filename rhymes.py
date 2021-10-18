def helper(phonemes1, phonemes2, idx1, idx2):

    before1 = phonemes1[:idx1]
    before2 = phonemes2[:idx2]
    after1 = phonemes1[idx1:]
    after2 = phonemes2[idx2:]
    minimum = min(len(before1),len(before2))

    if after1 == after2 and before1 != before2:
        if minimum == 0:
            return True
        if before1[-1] != before2[-1]:
            return True

    return False

def rhymes(phonemes1, phonemes2):
    
    idx1 = 0
    for phoneme1 in phonemes1:
        if phoneme1[-1] == '1':
            idx2 = 0
            for phoneme2 in phonemes2:
                if phoneme2[-1] == '1':
                    return helper(phonemes1, phonemes2, idx1, idx2)

                idx2 += 1
        idx1 += 1
        
    return False    

def main():
    list1 = ['AY1','Z']
    list2 = ['F','L','AY1','Z']

    bl = rhymes(list1, list2)
    print(bl)
    
if __name__ == "__main__":
    main()