#!/bin/usr/env python3

import pyexcel

# Request data from user
def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the drivr associated with this device?")
    d = {"IP": "172.16.2.10", "driver": input_driver}
    return d # Returns anything you ask it for outside of the function.  You can only have it only do once


## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the cfirst column, whereas driver is the second column.
## mylistdict = [ {"IP"" "172.16.2.10", "driver": "arista_eos"} ]
## {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")

# Runtime
mylistdict = [] # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data()) # add an item to the list \
    #returned by get_ip_data() {"IP": value, "driver": value}
    keep_going = input("\nWould you like to add another value? Enter \
    to continue, or enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name= filename )

print("The file " + filename + ".xls should be in your local directory")