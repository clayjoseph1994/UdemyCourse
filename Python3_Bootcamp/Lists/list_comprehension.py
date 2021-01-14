#Use a list of names with capitalized names and create a variable called answer that prints a new list containing only the first letter of each name.

#Use a list of values 1-6 and create a variable called answer2 that creates a list of all the even values in the list.

names = ["Elie", "Tim", "Matt"]
nums = [1,2,3,4,5,6]

answer = [person[0] for person in names]

answer2 = [num for num in nums if num % 2 == 0]

print(answer)
print()
print(answer2)