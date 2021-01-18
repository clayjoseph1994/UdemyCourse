# def print_square_of_7():
#     print(7*2)

# print_square_of_7()

def square_of_7():
    print("I AM BEFORE RETURN")
    return 7**2
    print("I AM AFTER RETURN")

result = square_of_7()
print(result)

#return does the following
#- exits the function
#- outputs whatever value is placed after the return keyword
#- pops the function off the call stack