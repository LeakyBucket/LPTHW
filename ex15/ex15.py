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

# Printing a line of instruction
print "Type the filename again:"
# Displaying a prompt and assigning the input to file_again
file_again = raw_input("> ")

# Opening the file provided by the user and stored in file_again.  Assigning that to txt_again.
txt_again = open(file_again)

# Printing the contents of txt_again
print txt_again.read()