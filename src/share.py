from subprocess import call, check_output
import sys
import re

# arbitary message to display the ip address
msg = 'go to -> {0}:8000\nPress ctrl+c to exit..\n\n'

# the commands to start the server
svr = ['python', '-m', 'simpleHTTPServer']

# in python 3 simpleHTTPServer was replaced by http.server
if sys.version_info.major == 3:
    svr[2] = 'http.server'


# get the output of the command 'ipconfig'
# and convert to a string, its return as bytes i think
out = str(check_output(['ipconfig']), encoding='utf-8')

# the pattern to search for to get the ip address
pattern = r'IPv4 Address.*: (?P<ip>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)'

# actually search the string for the pattern
# returns None if the pattern is not found
found = re.search(pattern, out)

# check to see if we have found the ip address
if found is not None:
    # get the ip part of the pattern
    ip = found.group('ip')
    print(msg.format(ip))

    # call the command to start the server
    call(svr)
else:
    # what to do if the ip address wasn't found
    print('Not Found...')
