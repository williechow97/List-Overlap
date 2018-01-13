# List Overlap
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] and write a program that returns a list that contains only 
# the elements that are common between the lists (without duplicates). Make sure your 
# program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don't worry if you can't figure this out at this point - we'll get to it soon)

import random # used to generate a random integer

def generateRanList():
    '''create two randomly generated list with values ranging from 0 - 99
       returns tuple of two list
    '''
    l1 = [elm for elm in range(random.randint(1,100))]
    l2 = [elm for elm in range(random.randint(1,100))]
    print('l1', l1)
    print('l2', l2)
    return (l1,l2)

def listOverlap(a,b):
    '''@param: a tuple of two list
        prints out a list of the overlap of the two list in the parameter tuple
    '''
    overlap = [elm for elm in a if elm in b]
    print('overlap',overlap)
    
def main():
    listOverlap(*generateRanList()) 

main()