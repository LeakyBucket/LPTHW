filename = raw_input("Which file do you want? ")

# Assigning txt to the file passed on the commandline
txt = open(filename)

# Printing the filename
print "Here's your file %r:" % filename
# Printing the contents of the file assigned to txt
print txt.read()