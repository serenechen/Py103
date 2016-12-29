name = 'Zed A. Shaw'
age = 35 # not a lie
height = round(74 * 2.54) # centimetres
weight = 180 * 0.453592 # kgs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %f centimetres tall." % height
print "He's %f kgs heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %f, %f, and %f I get %f." %(age, height, weight, age + height + weight)
