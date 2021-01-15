#Create two lists (1-4 and 3-6) and create a variable called answer that combines the two lists only by storing the values shared between the two lists
#Create a list of names that are capitalized and create a variable called answer2 that stores a new list of these names reversed (mitchell becomes llehctim) and lower-case

list_a = [1,2,3,4]
list_b = [3,4,5,6]

names = ["Elie", "Tim", "Matt"]

answer = [num for num in list_a if num in list_b]

answer2 = [name[::-1].lower() for name in names]

print(answer)
print(answer2)