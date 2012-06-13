# Include argv from the sys module
from sys import argv

# unpack argv
script, input_file = argv

# define the print_all method
def print_all(f):
  # print the contents of the provided file
  print f.read()

# define the rewind method
def rewind(f):
  # Move the IO Stream back to the beginning of the file (byte 0)
  f.seek(0)

# define the print_a_line method
def print_a_line(line_count, f):
  # print the line_count parameter and the next line from the provided file
  print line_count, f.readline()

# open input_file and assign it to current_file
current_file = open(input_file)

# print a static message
print "First let's print the whole file:\n"

# call print_all with current_file as the argument
print_all(current_file)

# print a static message
print "Now let's rewind, kind of like a tape."

# call rewind with current_file as the argument
rewind(current_file)

# print a static message
print "Let's print three lines:"

# set current_line to 1
current_line = 1
# call print_a_line with current_line and current_file as arguments
print_a_line(current_line, current_file)

# set current_line to 2
current_line = current_line + 1
# call print_a_line with current_line and current_file as arguments
print_a_line(current_line, current_file)

# set current_line to 3
current_line = current_line + 1
# call print_a_line with current_line and current_file as arguments
print_a_line(current_line, current_file)