#!/usr/bin/python
import sh
import sys

def printhelp():
    print "Usage: \"get-aperture LIST_TYPE FORMAT\""
    print "List types:"
    print " -a: print all the f-numbers, both current (marked with N) and possible (marked with P)"
    print " -c: print the current f-number"
    print " -p: print the available f-numbers"
    print "Formats:"
    print " -d: decimal values with dot"
    print " -v: decimal values with comma"
    sys.exit(3)

replacing = ","
if sys.argv[2] == "-d":
    replacing = "."

elif sys.argv[2] != "-v":
    printhelp()

out = sh.gphoto2("--get-config=f-number")

if sys.argv[1] == "-a":
    for line in out.splitlines():
        if b'Current:' in line:
            print "N", line.replace("Current: f/", "").replace(",", replacing)
            
        elif b'Choice:' in line:
            print "P", line.replace("Choice:", "").split("f/")[1].replace(",", replacing)
            
elif sys.argv[1] == "-c":
    for line in out.splitlines():
        if b'Current:' in line:
            print line.replace("Current: f/", "").replace(",", replacing)
            sys.exit(0)
            
elif sys.argv[1] == "-p":
    for line in out.splitlines():
        if b'Choice:' in line:
            print  line.replace("Choice:", "").split("f/")[1].replace(",", replacing)
            
else:
    printhelp()
