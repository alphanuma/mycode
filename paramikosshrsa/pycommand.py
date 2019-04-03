#!/bin/usr/env python3

import paramiko
import os

def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    
    return ssh_stdout.read().decode('utf8')


sshsession = paramiko.SSHClient()

sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sshsession.connect(hostname="10.10.2.3", username="bender", password="alta3" ) 

x = "uptime"

with open("benderdta.txt", "a") as bdata:
    timelog = (commandissue(x).lstrip().split(", "))
    exctime = (timelog[0].split())
       #print(exctime[0], exctime[2])
       #print(timelog[1])
    d = {"exec_time": exctime[0], "up_days": exctime[2], "up_hours_mins": timelog[1], "rightnow" } 
    mylist = (d)
    pyexcel.save_as(records=d, dest_file_name="benderlog.xls")
#print(commandissue(x).lstrip().split(","))

sshsession.close()
