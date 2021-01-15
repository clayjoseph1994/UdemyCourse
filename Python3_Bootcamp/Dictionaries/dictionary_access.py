# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

#Simply print out a string depending on whether food is a value in bakery_stock. If food is inthe bakery_stock dictionary, print a string that states how many items are left: ie "3 left" if the food is toffee cookie. If food is not contained in bakery_stock, print "We don't make that".

# YOUR CODE GOES BELOW:
print(food)
if food in bakery_stock:
    print("{} left".format(bakery_stock[food])) 
else:
    print("We don't make that")


    #This was one of the more difficult exercises I've done. I had a hell of a time trying to get the syntax right for the print statement showing what was left