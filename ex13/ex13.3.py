from sys import argv

argument = argv[1:2]

argument = raw_input("You said: %s? " % (argument[0]))

while argument != "shutup":
  argument = raw_input("Now you are saying: %s? " % (argument))