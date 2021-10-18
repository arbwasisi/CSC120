"""
Author: Arsene Bwasisi
Description: This program compares to musical composition and finds
             any similarity between them. It will taken in a file with
             songs and their composition and using the jaccard indexing
             algrothim rate their similarities between 0-1.
"""

def process_file(file):
    '''This function will open and process the file into a dictionary.'''

    file = open(file, 'r')
    music_comp = {}

    for line in file:
        # skip all empty spaces
        if line[0] != '\n':
            # grab the description line
            # if line is no the description
            # and musical notes to dictionary
            # with the description id as the key
            if line[0] == '@':
                ls = line.split()
            else:
                ls_2 = line.split()

                music_comp[ls[1]] = ls_2

    return music_comp

def ngrams(dic, n):
    """ 
    Function uses n-gram algorithm to return a set of tuples with 
    length n, containg the values in dic.
    """

    ngram_dic = {}

    for id_num, note_list in dic.items():

        ngram_set = set()
        startpos = 0
        endpos = n

        # loop through list to get n-grams from note_list
        # convert n-grams to tuple and add to set
        # increment the start and end positon
        while endpos<= len(note_list):
            sub_list = tuple(note_list[startpos:endpos])
            ngram_set.add(sub_list)
            endpos += 1
            startpos += 1

        # after all iteration and set to ngram_dic
        # with id_num as the key
        ngram_dic[id_num] = ngram_set

    return ngram_dic

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
    
def compute_score(pos1, pos2, score_list, ids_pair, id_list, ngram_dic):
    """ 
    Fuction will compute score of each set in ngram_dic using the
    jaccard function, and also keep track of each pair ids.
    """

    ids = []

    # store ids, at specifiend indexes, in variables
    id_num1 = id_list[pos1]
    id_num2 = id_list[pos2]
    score = jaccard(ngram_dic[id_num1], ngram_dic[id_num2])
    score_list.append(score)

    # create 2d list of id pairs
    ids.append(id_num1)
    ids.append(id_num2)
    ids_pair.append(ids)
    
    return score_list, ids_pair

def sim_score(ngram_dic, id_list):
    """ 
    Using the compute_score function, this function will return the;
    score_list: a list of all the calculated score
    ids_pair: a 2d list of the pair of ids that are compared
    """

    pos1 = 0
    pos2 = 1
    score_list = []
    ids_pair = []

    # if the size of a list is greater than two
    # loop through list, otherwise no loop is required
    if len(id_list) > 2:
        # while the first postion is not the last value,
        # keep iterating
        while id_list[pos1] != id_list[-1]:
            score_list, ids_pair = compute_score(pos1, pos2, score_list,\
            ids_pair, id_list, ngram_dic)

            # increment pos1 only when pos2 is the las value
            # reset pos2 as well if codition is true
            if id_list[pos2] == id_list[-1]:
                pos1 += 1
                pos2 = pos1 + 1
            else:
                pos2 += 1
    else:
        score_list, ids_pair = compute_score(pos1, pos2, score_list,\
        ids_pair, id_list, ngram_dic)

    return score_list, ids_pair

def find_max(score_list):
    """ Fuction finds and returns max score from max_list"""

    max_score = 0
    idx =  0

    # Keep track of max score and it's index value
    for score in score_list:
        if score > max_score:
            max_score = score
            max_i = idx

        idx += 1

    return max_score, max_i

def main():

    file = input('')
    ngram_sz = int(input(''))

    music_dic = process_file(file)
    ngram_dic = ngrams(music_dic, ngram_sz)

    id_list = list()
    for id_num in ngram_dic:
        id_list.append(id_num)

    score_list, ids_pair = sim_score(ngram_dic, id_list)
    max_score, max_idx = find_max(score_list)

    # use max_idx to locate the id pair with the max score
    # in ids_pair
    max_ids = ids_pair[max_idx]
    id_num1 = max_ids[0]
    id_num2 = max_ids[1]

    print("{} {} {:f}".format(id_num1, id_num2, max_score))

main()
