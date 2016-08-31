# Python program to crawl a website.

import re
import urllib

textfile = file('depth.txt', 'wt')
print "Enter the URL you wish to crawl"
print 'Usage - "http://example.com/" -> Make sure you put double quotes'
myurl = input(">>>")
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
        print i
        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                print ee
                textfile.write(ee+'\n')
textfile.close()