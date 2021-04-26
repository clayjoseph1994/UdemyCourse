#This program uses looping to print emojis on lines in the terminal
#It uses for loops and while loops to increment the emojis on each line
#a number of times specified by the range. I then tweaked it to center the 
#emojis using both for and while loop portions. The end result is 4 stacks of
#emoji icons, the 1st and 3rd of which are simply incremented.
#The 2nd and 4th stacks are centered.


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
