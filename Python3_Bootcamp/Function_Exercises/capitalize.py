#Write a function called capitalize that accepts a string and returns this string with
#the first letter capitalized. Use slices



'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(string):
    return string[:1].upper() + string[1:]

print(capitalize("test"))
print(capitalize("tim"))
print(capitalize("matt"))