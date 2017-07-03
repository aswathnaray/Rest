import webbrowser
import time

lnum = 1
print "This program started on " + time.ctime()
while lnum <= 3:
    time.sleep(2)
    webbrowser.open("http://www.bbc.com/news")
    lnum += 1
