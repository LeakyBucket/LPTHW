from sys import argv

one, two, three, four, last = argv[1:6]

print "Who cares what the script is called?"
print "Argument one is:", one
print "Argument two is:", two
print "Argument three is:", three
print "Argument four is:", four
print "The last argument I care about is:", last
print "Anything else has been ignored"