# Imports argv module from sys
from sys import argv

# Unpacks the argv by assigning it to script and filename
script, filename = argv

# Opens the file and stores the file object that has been returned to variable txt
txt = open(filename)

# Print filename's value and use read function to show the content
print "Here's your file %r:" % filename
print txt.read()

# Request the filename again
print "Type the filename again:"
file_again = raw_input("> ")

# Returns a new file object
txt_again = open(file_again)

# Read the file
print txt_again.read()

txt.close()
txt_again.close()

print "Two files have been closed."


# Study Drill Problems

# Trying to open ex15_sample.txt from Python Shell and got this error

# <open file 'ex15_sample.txt', mode 'r' at 0x104f32660>
