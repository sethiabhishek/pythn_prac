import os
import sys

modPath =  sys.modules['os.path']
print dir(modPath)
path = r'c:/'
for root,dirs,files in os.walk(path):
    print "root is %s:" %root
    print "dirs is %s:" %dirs
    print "files are %s" %files