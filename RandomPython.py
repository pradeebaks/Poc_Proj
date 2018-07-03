import random

#________________________________Randrange___________________________________________

#Randrange excludes the stop value from the search and randint includes the final values.

#print(random.randrange(10))

#print(random.randrange(10,14,2))

#__________________________________________Randint________________________________________

# print(random.randint(1,10))
# print(random.randrange(1,10))

# iter = 0
# while iter < 10:
#    r = random.randint(0,9)
#    print(r)
#    iter +=1

#_________________________________________Choice________________________________________


#print(random.choice(["india","pak","aus"]))
##
#print(random.choice([-1, 1, 3.5, 9, 15]))
##
#print(random.choice((1.1, -5, 6, 4, 7)))
##
##print(random.choice('Learn Python Programming'))

#__________________________________________Shuffle_____________________________________

# from random import shuffle
# ##
# mylist = [11,21,31,41,51]
# shuffle(mylist)
#
# print(mylist)

#____________________________________Sample_________________________________

# How to use sample() in Python?
#from random import sample

# Select any three chars from a string

#print(sample('Python',3))
##
### Randomly select a tuple of three elements from a base tuple
##
#print(sample((21, 12, -31, 24, 65, 16.3), 3))
##
### Randomly select a list of three elements from a base list
##
#print(sample([11, 12, 13, 14, -11, -12, -13, -14], 3))
##
### Randomly select a subset of size three from a given set of numbers
##
#print(sample({110, 120, 130, 140}, 3))
##
### Randomly select a subset of size three from a given set of strings
##
#print(sample({'Python', 'C++', 'Java', 'Go'}, 3))

#__________________________________Random Floating______________-

# How to generate a floating-point random number in Python?
import random
##
### Generate a floating-point pseudo-random number between 0 and 1.
##
# print(random())

#__________________________________Random Uniform_______________
##
##import random
##
# lower = 10; upper = 20
# random_float = random.uniform(lower, upper)
# print(random_float)

#__________________________Random Unifrom with Precision(Digits)

##import random
##
lower = 1.0; upper = 2.0; fixed_precision = 5

random_float = random.uniform(lower, upper)

print(round(random_float, fixed_precision))

