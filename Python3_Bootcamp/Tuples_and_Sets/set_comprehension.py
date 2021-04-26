string = "hello"
string1= "sequoia"
string2 = "Supercalifragilisticexpealidocious"

#var string2 can be subbed for string or string1 to check the bool value of the statement. 
#Does the string supplied include all 5 vowels?

x = len({char for char in string2 if char in "aeiou"}) == 5

print(x)