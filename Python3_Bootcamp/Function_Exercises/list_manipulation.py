#Write a function called list_manipulation that takes 4 parameters:
#(a list, command, location, and value)
#If command is remove and location is end, function should remove the last value in the list and return the value removed
#If command is remove and location is beginning, function should remove the first value in the list and return the value removed
#If command is add and location is beginning, function should add the value to the beginning of the list and return the list
#If command is add and location is end, function should add the value to the end of the list and return the list





'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(collection, command, location, value= None):
    if (command == "remove" and location == "end"):
        return collection.pop()
    elif (command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif (command == "add" and location == "beginning"):
        collection.insert(0, value)
        return collection
    elif (command == "add" and location == "end"):
        collection.append(value)
        return collection

print("First one:")
print(list_manipulation([1, 2, 3], "remove", "end"))
print("Second one:")
print(list_manipulation([1, 2, 3], "remove", "beginning"))
print("Third one:")
print(list_manipulation([1, 2, 3], "add", "beginning", 20))
print("Fourth one:")
print(list_manipulation([1, 2, 3], "add", "end", 30))