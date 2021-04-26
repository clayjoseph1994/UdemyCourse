#Write a function called multiply_even_numbers that accepts a list of numbers and
#returns the product of all even numbers in the list



'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(collection):
    yeet = 1
    for value in collection:
        if value % 2 == 0:
            yeet = yeet * value
    return yeet

print(multiply_even_numbers([2,3,4,5,6]))