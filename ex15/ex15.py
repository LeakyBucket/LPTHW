# Adding argv from the sys module
from sys import argv

# Assigning commandline arguments to local variables
script, filename = argv

# Assigning txt to the file passed on the commandline
txt = open(filename)

# Printing the filename
print "Here's your file %r:" % filename
# Printing the contents of the file assigned to txt
print txt.read()