#!/usr/bin/python3

list_ips = ["10.2.16.2", "10.2.16.45", "10.16.2.131", "10.16.2.122"]

x = 0 

#while x < 4:
#    print(list_ips[x])
#    x+= 1
#x += 1 #x = x+1
#print("All done")
#server_names =["srv1", "srv2", "srv3", "srv4"]
#i is for interator
#for i in server_names:
#	print(i)

my_file = open("cloud.txt", "r")

for line in my_file:
    print(line, end="")

my_file.close()
