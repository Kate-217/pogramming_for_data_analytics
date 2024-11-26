# Lab # 01
# Author Kate Lisovenko
# Write a program to read in the data in data.csv and output each line as a list.

import csv


FILENAME= "data.csv"
DATADIR="programming_for_data_analytics/my_work/"
# DATADIR="../my_work/"


with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=',')
    for line in reader:
        print (line)
        

# Modify the program to deal with the header line separately

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if linecount == 0: # first row in header row
            print (f"{line}\n-------------------")
        else: # all subsequent rows
            print (line)
        linecount += 1
print(linecount)    

#  Modify the program to calculate the average age, there are a few ways to
# solve this;
# a. Convert the string that is read into an integer

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # the same as "if linecount == 0"
            pass
        else: # all subsequent rows
            
            total += int(line[1]) # [1] is second column 
        linecount += 1
    print (f'Average age is {total/(linecount-1)}') # - 1 , because linecount counts header
    
# b. Use the quote parameter to read in the numbers as floats
    
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # the same as "if linecount == 0"
            pass
        else: # all subsequent rows
            total += line[1] # [1] is second column 
        linecount += 1
    print (f'Average age is {total/(linecount-1)}')     
    
# 7. Write a program to print this JSON to the console.

import requests
url ="https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data)
print(type(data)) # json returns dict
# 8. Modify the program to only output the current price in Euros.

print(data['bpi']['EUR']['rate_float'])

