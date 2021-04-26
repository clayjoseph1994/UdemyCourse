# Write a function called multiple_letter_count that takes onne parameter (a string) and returns a dictionary with the keys being
# the letters and the values being the count of the letter. Hint: use a dictionary comprehension and count()

'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# define multiple_letter_count:
def multiple_letter_count(str):
    print(f"Dictionary of letters and number of times they appear in the word {str}: ")
    return {letter: str.count(letter) for letter in str}

print(multiple_letter_count("awesome"))