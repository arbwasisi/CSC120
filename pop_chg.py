# Author: Arsene Bwasisi
# Description: This program will take in a file of the population 
#              US state between 2010-2019, and calculate the maximum change

def process_file(file):
    '''This function will open and process the file into a list.'''
    
    read_file = open(file, 'r')
    read_file.readline()# bypass first line
    
    state = str()
    us_states = list()
    change_array = list()
    
    for line in read_file:
        split_line = line.split()# split line into list

        # Calculate the rate of change between 2010-2019
        pop_change=(int(split_line[-2])-int(split_line[-1]))/int(split_line[-1])
        change_array.append(pop_change)# append rate to list

        # Combines state name if divide by split function
        sliced_array = split_line[:-2]
        for name in sliced_array:
            if name != sliced_array[-1]:
                state += name + ' '
            else:
                state += name

        us_states.append(state)# append state name to list
        state = '' # reset empty string
    
    return change_array, us_states

def compute_max(change_array, us_states):
    '''
    This function cumputes the maximum population change, and keeps track
    of any tie. It stores the result in a list. 
    '''
    
    maximum = change_array[0] # set maximum rate to first value in list
    maximum_change = [change_array[0]]# list that will hold maximum rate
    maximum_state = [us_states[0]]# list that will hold maximum states

    # Check for maximum, and remove vaule in maximum_change list
    # if maximum is less then current index value 
    for index in range(1,len(change_array)):
        if change_array[index] >= maximum:
            if change_array[index] > maximum:
                maximum = change_array[index]
                maximum_change.append(maximum)
                maximum_state.append(us_states[index])
                del maximum_change[:-1]
                del maximum_state[:-1]
            else: # checks for tie
                maximum = change_array[index]
                maximum_change.append(maximum)
                maximum_state.append(us_states[index])
                
    return maximum_change, maximum_state
                
def main():
    
    file = input('')
    change_array, us_states = process_file(file)
    maximum_change, maximum_state = compute_max(change_array, us_states)
    
    index = 0
    for name in maximum_state:
        print("{}: {:f}".format(name, maximum_change[index]))
        index += 1
        
main()

