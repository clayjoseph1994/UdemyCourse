# Write a function called number compare. This function takes in two parameters (both numbers). If the first is greater than the 
# second, this functionr eturns "First is greater". If the second number is greater, it returns "Second is greater". Otherwise,
# the function returns "Numbers are equal"

'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(num1, num2):
    if num1 > num2:
        return "First is greater"
    elif num1 < num2:
        return "Second is greater"
    else:
        return "Numbers are equal"

print(number_compare(1,5))
print(number_compare(5,1))
print(number_compare(3,3))