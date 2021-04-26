def sum_all_nums(num1, num2, num3):
    return num1+num2+num3

print("This is using multiple specified parameters in the function definition")
print(sum_all_nums(1,2,3))
print("============================================================")

def sum_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

print()
print("This is using the *args parameter to pass in a single value for args in the definition and specify multiple args in the function call")
print(sum_nums(4,6,9,4,10,15))
print("============================================================")

def contains_purple(*colors):
    if "purple" in colors: return True
    return False

print()
print("Contains purple?")
print(contains_purple("blue", "green", "Yellow"))
print("Contains purple?")
print(contains_purple("orange", "magenta", "purple"))