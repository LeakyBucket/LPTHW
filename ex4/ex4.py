# Initialize the number of cars
cars = 100
# Initialize the amount of space in a car
space_in_a_car = 4.0
# Set the number of drivers
drivers = 30
# Set the number of passengers
passengers = 90
# Determine how many more cars we have than drivers
cars_not_driven = cars - drivers
# Set the number of cars driven to be equal to the number of drivers
cars_driven = drivers
# Determine the total number of people that can be moved
carpool_capacity = cars_driven * space_in_a_car
# Determine how to evenly distribute passengers amongst cars
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."