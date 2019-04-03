#!/bin/usr/env python3

import pyexcel

# Request data from user
def get_ip_data():
    mylist = []
    with open("flat.txt", "r") as myfile:
        for row in myfile:
            myrow = row.split()
            d = {"IP": myrow[0], "driver": myrow[2], "port": myrow[3]}
            mylist.append(d)
    return mylist # Returns anything you ask it for outside of the function.  You can only have it only do once


## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the cfirst column, whereas driver is the second column.
## mylistdict = [ {"IP"" "172.16.2.10", "driver": "arista_eos"} ]
## {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")

# Runtime
mylistdict = [] # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")
data = (get_ip_data()) # add an item to the list \
    #returned by get_ip_data() {"IP": value, "driver": value}
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name= filename + "*.xls" )

print("The file " + filename + ".xls should be in your local directory")
