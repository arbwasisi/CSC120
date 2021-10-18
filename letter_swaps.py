def helper(text, swapped, idx_1, idx_2):

    letters = []
    string = ''

    for letter in text:
        letters.append(letter)
            
    letters[idx_1], letters[idx_2] = letters[idx_2], letters[idx_1]
        
    for letter in letters:
        string += letter
        
    if string != text:
        swapped.append(string)

    return swapped

def letter_swaps(text):
    
    swapped = []
    idx_1 = 0
    idx_2 = 1
    
    while text[idx_1] != text[-1]:
        swapped = helper(text, swapped, idx_1, idx_2)

        if text[idx_2] == text[-1]:
            idx_1 += 1
            idx_2 = idx_1 + 1
        else:
            idx_2 += 1
            
    return sorted(swapped)
            
def main():
    
    swapped = letter_swaps('foo bar')
    print(swapped)
    
if __name__ == "__main__":
    main()
    