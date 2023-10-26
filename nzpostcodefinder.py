# New Zealand Postcode finder
# IMPORTANT! Needs the file postcodes.csv to be placed in the same folder as this file to run.
# Can be modified to run Searches on any Country by changing the.csv file
# Works in Python 3 - Does not work in Python 2


# import the modules we need to run the program
# csv modules reads .csv (comma seperated value) data files  
# webbrowser modules for opening the web page
# sys module for exit function
# time module for sleep function to wait 2 seconds on exit

import csv
import webbrowser
import sys
import time

# creates function to be used for quiting program
def goodbye():
    print('\n----------------------------------------------------------------------')
    print('Thanks for using the New Zealand Postcode Locator and Place Name Finder')
    print('----------------------------------------------------------------------\n')
    print('Bought to you by BR88')
    time.sleep(2)
    sys.exit(0)

# creates a message to say Postcode or Place not on List
def not_found():
    print('\n\n-----------------------------------------------------------')
    print('That Place Name or Postcode was not in the list. Try again.')
    print('-----------------------------------------------------------\n\n')

# creates a function to say option not on list
def not_on_list():
    print('\n\n------------------------------------------------------------')
    print('That selection does not match any of the options. Try Again.')
    print('------------------------------------------------------------\n\n')
    
    
# creates welcome message
def welcome():
    print('\n--------------------------------------------------------------------')
    print('Welcome to the the New Zealand Postcode Locator and Place Name Finder')
    print('--------------------------------------------------------------------\n')
    print('-----------------------------------------------------------------------------------------')
    print('Make sure Python3 is installed. Does not work with Python 2\n')
    
    print('Shows the Postcode for New Zealand  Cities, Suburbs and Regional Place Names.')
    print('Shows the approximate Latitude and longitude for a given Postcode or Location')
    print('Shows how many other Locations in New Zealand  also share the same Name and Postcode.')
    print('Shows Postcode or Places location on a Map. Opens a webpage so needs internet connection.')
    print('Works with either upper or lowercase letters however spelling or place names MUST be correct.')

    print('------------------------------------------------------------------------------------------\n\n')

# main part of program

welcome()

# creates main loop that runs until user selcts 'q'
loop1 = 1
while loop1 == 1:
    found = False
    
# creates loop to ask for user input, search the csv file, print and store the results for later opening a webpage 
    loop2 = 1
    while loop2 == 1:
        burb = input('\nEnter a Postcode or the name of a City, Town or Suburb: ')
        
# if user select q call goodbye function
        if burb.lower() == 'q':
            goodbye() 

# reads the data in the postcodes .csv file
        with open("nz_postcodes.csv", 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
                       
# creates a list to store the search results. 'x' is a counter to be used in assigning a number next to each found place name
            x=1
# creates an empty list for storing URLS of each found place
            list_map_link = []
            
# searches through each row of .csv file - the .lower function takes any text and converts uppercase to lowercase for searching
            for row in csv_reader:
                if row[1].lower() == burb.lower() or row[0] == burb:
                    found = True
                    
# each row{x} corresponds to a column in the csv file for place_name, postcode etc
                    print('\n',x,row[1],'\n\r',row[2],row[0],'\n','latitude ',row[4],' longitude ',row[5],'\n')
                    
# creates a string called map_link which uses lat and long values from csv file and concatenates into a single URL 
                    map_link = 'https://osmand.net/map/?pin=' + str(row[4]) +',' + str(row[5]) + '#7/' + str(row[4]) + '/' + str(row[5])
                    
# appends each search result into a listof Urls for opening maps                 
                    list_map_link.append(map_link[:])
                    
# sets x as a counter for the number of found search results                    
                    x +=1
                    
# If place name or other user input not found in list                                        
            if found != True:
                not_found()

# ends the data search loop                   
            loop2 = 0
        
# creates a loop to allow user to select which suburb to open in a mapor quit      
    loop3 = 1
# creates a variable for converting the select_options variable from a string to an integer for later use
    i=0
    
    while loop3 == 1:
        print('------------------------------------')
        print('Select from the Following Options :-')
        print('------------------------------------\n')
        print('     Number - Left of Place Name (eg 1) to open a webpage to show location on a map.')
        print('              must be connected to the internet to work\n')
        print('     Enter  - Do another Place or Postcode search\n')
        print('     Q      - quit\n')

# asks for user input
        select_options = input('')
        
# if check to see if selection is a number and is found
        if select_options.isdigit() and found == False:
            not_found()      
            
# gets number of urls stored in list for later use        
        size = len(list_map_link)
        
# If user selects q calls goodbye function    
        if select_options.lower() == 'q' or burb.lower() =='q':
            goodbye()
            
# checks that user input is both a number and not bigger than the number of URLs stored in list before opening webpage            
        if select_options.isdigit() and int(select_options) < x:
            i = int(select_options)-1
            if i <= size :
                webbrowser.open(list_map_link[i])
                
# checks that user input is enter key - an '' which loops back to start              
        if select_options == '':
            loop3 = 0
 
# closes off loop 3 which send program back to the start - loop 1
        
        else:
            not_on_list()
            loop3 = 0
            
# loop 1 is never actually closed so program runs until user selects 'q' to quit




            
        
        
            
       
                
                
                    
              






        


