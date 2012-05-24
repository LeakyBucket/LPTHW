# Setting x to a formatted string
x = "There are %d types of people." % 10
# Setting binary to the string "binary"
binary = "binary"
# Setting do_not to the string "don't"
do_not = "don't"
# Setting y to a formatted string with two substitutions
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing x
print x
# Printing y
print y

# Printing a formatted string containing the string assigned to x
print "I said: %r" % x
# Printing a formatted string containing the string assigned to y
print "I also said: '%s'." % y

# Setting hilarious to False
hilarious = False
# Setting joke_evaluation to a string that will accept a formatting argument
joke_evaluation = "Isn't that joke so funny?! %r"

# Printing joke_evaluation and using hilarious for the formatting replacement
print joke_evaluation % hilarious

# Setting w to a vanilla string
w = "This is the left side of..."
# Setting e to a vanilla string
e = "a string with a right side."

# Printing the concatination of w and e
print w + e