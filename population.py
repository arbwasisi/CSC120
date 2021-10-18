# Author: Arsene Bwasisi
# Description: This program will take in a file as 
#			   input and calculate its total population

def sum_pop(fobj):
    population = 0 #set population value to zero
    for line in fobj:
        array = line.split()# split each line into a list
        population += int(array[-1]) #increment the population value
        
    return population
    
def main():
    
    file = input('')
    read_file = open(file, 'r')
    result = sum_pop(read_file)
    
    print(result)
    
main()