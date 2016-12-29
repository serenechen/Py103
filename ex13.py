from sys import argv

#script, first, second, third = argv

#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

# Study Drill
age = raw_input("How old are you?")
height = raw_input("How tall are you?")
age, height = argv

print "So you are ", age, " years old and ", height, " tall."

#(Failed)
