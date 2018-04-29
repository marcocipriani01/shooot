#!/usr/bin/python
import sh
import sys

out = sh.gphoto2("--get-config=f-number")
#1: print all the f-numbers, both current (marked with N) and possible (marked with P)
#2: print the current f-number
#3: print the available f-numbers
if sys.argv[1] == "1":
    for line in out.splitlines():
        if b'Current:' in line:
            print "N", line.replace("Current: f/", "")
            
        elif b'Choice:' in line:
            print "P", line.replace("Choice:", "").split("f/")[1]
            
elif sys.argv[1] == "2":
    for line in out.splitlines():
        if b'Current:' in line:
            print line.replace("Current: f/", "")
            sys.exit(0)
            
elif sys.argv[1] == "3":
    for line in out.splitlines():
        if b'Choice:' in line:
            print  line.replace("Choice:", "").split("f/")[1]
