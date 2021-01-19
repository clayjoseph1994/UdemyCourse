print("This is the result of printing the output of the first function: ")
#an example illustrating that you can assign the arguments in any order using the keyword of the parameter set in the function
def full_name(first, last):
    return f"Your name is {first} {last}"

print(full_name("Joseph", "Clay"))
#here I am calling the function print to print what's returned by the full_name function
#I have set the args in the opposite order, but since I stated last="Clay" and first="Joseph", it doesn't matter what order I 
#add the args in the function call, because the order I specified to the parameters of the defined function is the order they appear
print("\nThis is the result of printing the first function after specifying keyword arguments in a different order: ")
print(full_name(last="Clay", first="Joseph"))

##when defining a function (ei def full_name(first, last)) and you use an = you're setting a default parameter
#when you invoke or call a function (ie fullname("Joseph", "Clay")) and use an equal sign here
#you are making a keyword arg that corresponds to the parameter of the defined function
print()
print("*" * 80)

def full_name1(first="Joseph", last="Clay"):
    return f"Your name is {first} {last}"
#showing the default, which is set by the default parameters
print()
print("This is the result of printing the output of the second function which specifies default parameters: ")
print(full_name1())
#showing the use of keyword args
print()
print("This is the result of printing the output of the second function after using keyword args to assign different values: ")
print(full_name1(last="Enthusiast", first="Python"))
