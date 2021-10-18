def helper(last, dic_words, phonemes):

    for letter in last:
        some_set = set()
        for array in dic_words:
            if letter == array[-1]:
                some_set.add(array[1])
                
        phonemes[letter] = some_set
    
    return phonemes

def build_rev_index(fileobj):

    last = []
    dic_words = []
    phonemes = {}

    for line in fileobj:
        if line != '\n':
            split_line = line.split()
            dic_words.append(split_line)
        
            if split_line[-1] not in last:
                last.append(split_line[-1])
    
    return helper(last, dic_words, phonemes)

def main():
    
    file = open('text.txt', 'r')
    build_rev_index(file)
    
if __name__ == "__main__":
    main()
    