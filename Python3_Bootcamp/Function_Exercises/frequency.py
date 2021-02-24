#Write a function called frequency that accepts a list and a search_term
#This function should return the number of times the search_term appears in the list



'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(collection, search_term):
    return collection.count(search_term)

print(frequency([1,2,3,4,4,4], 4))
print(frequency([True, False, True, True], False))