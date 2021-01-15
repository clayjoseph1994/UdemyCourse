#Using nested list comprehension create a variable called answer with the following value: [0, 1, 2], [0, 1, 2], [0, 1, 2]

answer = [[x for x in range(0,3)] for x in range(0,3)]
print(answer)

#Another one, but this creates a list of ten lists containing numbers 0-9 
answer2 = [[x for x in range(0,10)] for x in range(0,10)]
print(answer2)

