#!/usr/bin/python
import sh
import sys

out = sh.gphoto2("--get-config=iso")

if sys.argv[1] == "-a":
    for line in out.splitlines():
        if b'Current:' in line:
            print "N", line.replace("Current: ", "")
            
        elif b'Choice:' in line:
            print "F", line.replace("Choice:", "").split(" ")[2]
            
elif sys.argv[1] == "-c":
    for line in out.splitlines():
        if b'Current:' in line:
            print line.replace("Current: ", "")
            sys.exit(0)
            
elif sys.argv[1] == "-p":
    for line in out.splitlines():
        if b'Choice:' in line:
            print  line.replace("Choice:", "").split(" ")[2]
            
else:
    print "Usage: \"python2.7 iso-extractor.py OPTION\""
    print "Options:"
    print " -a: print all the ISO values, both current (marked with N) and possible (marked with F)"
    print " -c: print the current ISO value"
    print " -p: print the available ISO values"
    sys.exit(3)
