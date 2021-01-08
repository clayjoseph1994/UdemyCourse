#For loop
for x in range(1,11):
	print("\U0001f600" * x)
#For loop centered
lg = 10
sm = 1
user = range(1,11)
for x in user:
	space = " " * (lg - sm)
	print(space + "\U0001f600" * x)
	sm += 1
#While loop 
emoji = 1
while emoji <= 10:
	print("\U0001f600" * emoji)
	emoji += 1
#While loop centered
largest = 10
emoji = 1
while emoji <= largest:
	space = " " * (largest - emoji)
	art = "\U0001f600" * emoji
	print(space + art)
	emoji += 1
