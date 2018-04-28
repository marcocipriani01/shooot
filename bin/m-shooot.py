#!/usr/bin/python
import os
import errno
from time import sleep
import sys
import sh

name = sys.argv[1]

try:
    os.makedirs(name)
    
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

os.chdir(name)
print "Working in ", os.getcwd()

name = name.split(os.sep)[-1]
number = int(sys.argv[2])
fileformat = "." + sys.argv[3]
time = sys.argv[4]
sh.gphoto2("--set-config", "shutterspeed=" + time)
wait = float(time.replace(",", ".").replace("s", ""))
sh.gphoto2("--set-config", "f-number=" + sys.argv[5])
sh.gphoto2("--set-config", "iso=" + sys.argv[6])

for index in range(0, number):
    print index + 1, "of", number
    sh.gphoto2("--capture-image-and-download", "--filename=" + name + str(index) + fileformat, "--force-overwrite")
