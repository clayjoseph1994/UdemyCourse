#Write a function called is_palindrome that checks whether a string passed in is a 
#palindrome. A palindrome is a sequence of characters that reads the same 
#backward as it does forward (tacocat, hannah, etc.)
#Function should take in one parameter and return true or false
#as a bonus, allow the function to ignore whitespace and capitalization




'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(string):
    stripped = string.replace(" ", "") #gets rid of spaces
    final = stripped.lower() #ignore capitalization
    return final == final[::-1]


print(is_palindrome('testing'))
print(is_palindrome('tacocat'))
print(is_palindrome('hannah'))
print(is_palindrome('Hannah'))
print(is_palindrome('robert'))
print(is_palindrome('A man a plan a canal Panama'))