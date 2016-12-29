# Assign a string to x
x = "There are %d types of people." % 10
# Assign a string to binary
binary = "binary"
# Assign a string to do_not
do_not = "don't"
# Assign a string to y
y = "Those who knows %s and those who %s." % (binary, do_not)

# Print x
print x
# Print y
print y

# Print a string + value of x
print "I said: %r." % x
# Print a string + value of y
print "I also said: '%s'." % y

# Assign False to hilarious
hilarious = False
# Assign a string to joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# Print a string + the value of hilarious
print joke_evaluation % hilarious

# Assign a string to w
w = "This is the left side of..."
# Assign a string to e
e = "a string with a right side."

# print a string concating w and e
print w , e
