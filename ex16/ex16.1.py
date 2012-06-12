from sys import argv

target = open(argv[1:][0], "r")

print "So far you have:\n\n%s" % target.read()