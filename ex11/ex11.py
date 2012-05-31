print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old %r tall and %r heavy." % (age, height, weight)

# raw_input takes an optional string argument which will be displayed as a prompt
#   it then reads from STDIN until it sees a new line.  The stream is converted
#   to a string.  The trailing newline is stripped from the input.

print raw_input('Echo> ')