def add(a, b):
  print "ADDING %d + %d" % (a, b)
  return a + b

def subtract(a, b):
  print "SUBTRACTING %d - %d" % (a, b)
  return a - b

def multiply(a, b):
  print "MULTIPLYING %d * %d" % (a, b)
  return a * b

def divide(a, b):
  print "DIVIDING %d / %d" % (a, b)
  return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d ID: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# 35 + (74 - 180 * (50/2))
#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#what = add(age, multiply(height, subtract(weight, divide(iq, 2))))

# (22 * 33 / 4) + 10202
what = add(divide(multiply(22, 33), 4), 10202)

print "That becomes: ", what, "Can you do it by hand?"