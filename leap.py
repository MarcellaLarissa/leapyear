#Marcella Petrucci
#petrucma@oregonstate.edu
########################
#Program Description
# This program takes input from the user (a year) and evaluates wether it is a leap year or not
# Please run using Python 3 with the command: python3 leap.py
###########################import time
import numpy as np
import math
import re, sys

#Years that are evenly divisible by 4 
#except years that are evenly divisible by 100
#unless the years are also evenly divisible by 400



#validation loop
while(True):
    #take input
    userInput = input("Please enter a year as a valid integer starting at year 0.\n")
    print(" ")
    #check for valid input, cast to integer
    try:
        year = int(userInput)
    except:
        print(f'{userInput} is not a valid numerical input')
        print(" ")
        continue
    #check year range, if yes, exit loop 
    if(year >= 0):
        break
    #case if not in range, return to top of loop
    else:
        print(f'{userInput} is not a valid year')
        continue


#Years that are evenly divisible by 4
if(year%4 == 0):
    #case of leap years less than year 100
    if(year < 100):
        print(f'{year} is a leap year!')
        
    #case of years greater than 100 -- possible leap year
    elif(year%100 == 0):    
        # case of years are evenly divisible by 400 -- leap year
        if(year%400 == 0):
            print(f'{year} is a leap year!')
            
        #years that are evenly divisible by 100 -- no leap year
        else:
            print(f'{year} is NOT a leap year!')
    #years that are evenly divisible by 4 but not 100 -- leap year
    else:
            print(f'{year} is a leap year!')
            
#Years that are NOT evenly divisible by 4            
else:
    print(f'{year} is NOT a leap year!')            