# define the cheese_and_crackers method
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  # print the value of the cheese_count argument
  print "You have %d cheeses!" % cheese_count
  # print the value of the boxes_of_crackers argument
  print "You have %d boxes of crackers!" % boxes_of_crackers
  # print a static message
  print "Man that's enough for a party!"
  # print another static message
  print "Get a blanket.\n"


def echo(repeat):
  print repeat


# print a static message
print "We can just give the function numbers directly:"
# call cheese_and_crackers setting cheese_count to 20 and boxes_of_crackers to 30
cheese_and_crackers(20, 30)

# print a static message
print "OR, we can use variables from our script:"
# set amount_of_cheese to 10
amount_of_cheese = 10
# set amount_of_crackers to 50
amount_of_crackers = 50

# call cheese and crackers with the values of amount_of_cheese and amount_of_crackers as parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers) # Python basically creates new references to the data so is passing a reference

# print a static message
print "We can even do math inside too:"
# call cheese and crackers with 30 for cheese_count and 11 for boxes_of_crackers
cheese_and_crackers(10 + 20, 5 + 6)

# print static message
print "And we can combine the two, variables and math:"
# call cheese_and_crackers with 110 for cheese_count and 1050 for boxes_of_crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

for x in range(10):
  echo(raw_input('... '))