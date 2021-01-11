import random

random_number = random.randint(1,10)
guess = None

while guess != random_number:
	guess = input("Guess a random number between 1 and 10: ")
	guess = int(guess)
	if guess < random_number:
		print("Guess too low. Try agin. ")
	elif guess > random_number:
		print("Guess too high. Try again. ")
	else:
		print("Bitch, you guessed it. You was right!")
		again = input("Play again? (y for yes, anything else to quit): ")
		if again == "y":
			random_number = random.randint(1,10)
			guess = None
			print("******************************************")
		else:
			print("See you later!")
			break