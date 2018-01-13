#!/usr/bin/python
import sh
import sys

def printhelp():
    print "Usage: \"python2.7 shutter-speed-extractor.py LIST_TYPE FORMAT\""
    print "Options:"
    print " -a: print all the shutter speeds, both current (marked with N) and possible (marked with F)"
    print " -c: print the current shutter speed"
    print " -p: print the available shutter speeds"
    print "Formats:"
    print " -d: make decimal values use the dot"
    print " -v: let decimal values use the comma"
    sys.exit(3)

replacing = ","
if sys.argv[2] == "-d":
    replacing = "."

elif sys.argv[2] != "-v":
    printhelp()

out = sh.gphoto2("--get-config=shutterspeed")

if sys.argv[1] == "-a":
    for line in out.splitlines():
        if b'Current:' in line:
            print "N", line.replace("Current: ", "").replace(",", replacing)
            
        elif b'Choice:' in line:
            print "F", line.replace("Choice:", "").split(" ")[2].replace(",", replacing)
            
elif sys.argv[1] == "-c":
    for line in out.splitlines():
        if b'Current:' in line:
            print line.replace("Current: ", "").replace(",", replacing)
            sys.exit(0)
            
elif sys.argv[1] == "-p":
    for line in out.splitlines():
        if b'Choice:' in line:
            print  line.replace("Choice:", "").split(" ")[2].replace(",", replacing)
            
else:
    printhelp()
