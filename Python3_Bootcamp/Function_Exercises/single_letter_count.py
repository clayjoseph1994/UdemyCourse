# Write a function called single_letter_count. This functions takes in two parameters (two strings). The first parameter should be a 
# string and the second should be a letter. The function returns the number of times the letter appears in the word.
# It should be case-insensitive. If the letter is not found int he word, the function should return 0.
# Hint- take advantage of the count() method

#define single_letter_count below:
def single_letter_count(w, l):
    num = w.upper().count(l.upper())
    print(f"The letter {l} appears {num} times in {w}")

single_letter_count("Hello World", "h")
single_letter_count("Hello World", "l")

