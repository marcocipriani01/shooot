#!/usr/bin/python
import sh
import sys

out = sh.gphoto2("--get-config=imagequality")

if sys.argv[1] == "-a":
    for line in out.splitlines():
        if b'Current:' in line:
            print "N", line.replace("Current: ", "")
            
        elif b'Choice:' in line:
            print "P", line.replace("Choice:", "").split(" ")[2]
            
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
    print "Usage: \"get-iso OPTION\""
    print "Options:"
    print " -a: print all the image formats, both current (marked with N) and possible (marked with P)"
    print " -c: print the current image format"
    print " -p: print all the available image formats"
    sys.exit(3)
