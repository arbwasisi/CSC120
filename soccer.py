# Author: Arsene Bwasisi
# Description: This program will use a file of the US women soccer team,
#              the user will provide a start and stop time, and the program
#              print who had the most athlete of the year award.

def process_file():
    '''
    This functions opens the US women soccer team data file and
    collects the years and athlete of the year winners.
    '''

    file = open('data.csv', 'r')
    file.readline()# bypass comment line
    years = []
    athletes = []

    # loop through each line and split each line into a list
    # and collect the first and sixth vaules
    # append the values into the years and athletes list
    for line in file:
        array = line.strip('\n').split(',')
        years.append(array[0])
        athletes.append(array[5])
        
    return years, athletes
    
def compute(start, end, years, athletes):
    '''
    This function will check the athlete with the most awards
    within the dates provided
    '''    

    count = dict()#empty dictionaries that counts number of awards

    # Get index of the provided dates and slice throufh the 
    # players and years list
    index = years.index(start)
    index_2 = years.index(end)
    timeline = years[index:index_2+1]
    players = athletes[index:index_2+1]

    # Loop through sliced athletes list and keep track
    # of the number of time a player appears
    for player in players:
        if player not in count:
            count[player] = 0
        count[player] += 1

    # Set maximum value to the first item in the dictionaries
    # and build a list to keep track of players
    maximum = count[players[0]]
    maximum_list = [players[0]]

    # Loop through the dictionary to check if a value at each 
    # iteration is greater or equal than the current maximum
    # if true, added to maximum list
    for key in count:
        if key != players[0]:
            if count[key] >= maximum:
                if count[key] == maximum:
                    maximum_list.append(key)
                else:
                    maximum = count[key]
                    maximum_list.append(key)
                    # delete any item in list if less than
                    # current iteration value
                    del maximum_list[:-1]

    # sort content in the list
    sort_list = sorted(maximum_list)
    
    for name in sort_list:
        print(name)
    
def main():
    
    years, athletes = process_file()
    start = input('')
    end = input('')

    # Set out of rage input
    if int(start) < 1985:
        start = '1985'
    if int(end) > 2018:
        end = '2018'
    
    # Try compute(), if error produced end program   
    try:
        compute(start, end, years, athletes)
    except:
        pass
     
main()
    