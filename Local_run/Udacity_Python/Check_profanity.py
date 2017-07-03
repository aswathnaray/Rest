# read text

import urllib

def read_text():
    pc_open = open("C:\Workspace_py\Local_run\Udacity_Python\pcheck.txt")
    pc_read = pc_open.read()
    print pc_read
    pc_open.close()
    check_profanity(pc_read)

# check text

def check_profanity(sometext):
    cpurlopen = urllib.urlopen("http://www.wdylike.appspot.com/?q="+str(sometext))
    cpurlread = cpurlopen.read()
    print cpurlread
    cpurlopen.close()

read_text()