#Write a function called intersection that accepts two lists and returns a list with
#values that are in both lists only


# flesh out intersection pleaseeeee
def intersection(list1, list2):
    return [val for val in list1 if val in list2]

print(intersection([1,2,3,4,5,6,7,8,9], [1,3,4,16,20,5,7,14,32]))