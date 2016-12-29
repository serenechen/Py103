# Assign 100 to variable cars
cars = 100
# Assign 4.0 to variable space_in_a_car
space_in_a_car = 4.0
# Assign 30 to variable drivers
drivers = 30
# Assign 90 to variable passengers
passengers = 90
# Assign the value of cars minus drivers to variable cars_not_driven
cars_not_driven = cars - drivers
# Assign the value of drivers to variable cars_driven
cars_driven = drivers
# Assign the value of cars_driven mutiplies space_in_a_car to space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# Assign the value of passengers divided by cars_driven to variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# Study Drill

# line 8 car_pool-capacity made a typo after "car" where should be no underscores

# 4.0 for space_in_a_car is unecessary because the value of space in a car should always be integer
