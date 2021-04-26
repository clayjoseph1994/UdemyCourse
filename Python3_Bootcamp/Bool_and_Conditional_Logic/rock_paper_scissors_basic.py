#Tried and true game of rock, paper, scissors in the command line.
#The goal of this program is to demonstrate comprehension of boolean logic.
#This is the simple version where there are 2 users battling it out on the same terminal.
print("Rock...")
print("Paper...")
print("Scissors...")

print("Please enter name for Player 1: ")
p1_name = input()

print("Please enter name for Player 2: ")
p2_name = input()

p1 = input("Player 1, make your move. Choose 'rock', 'paper', or 'scissors': \n")
print("**********NO CHEATING***********\n\n" * 20)
p2 = input("Player 2, make your move. Choose 'rock', 'paper', or 'scissors': \n")

#Tie game
if p1 == p2:
	print("Tie Game. Try again!")
#p1 as rock
elif p1 == "rock":
	if p2 == "paper":
		print("Paper covers rock; " + p2_name + " wins!")
	elif p2 == "scissors":
		print("Rock crushes scissors; " + p1_name + " wins!")
	else:
		print(p2_name + "- Something went wrong; Maybe check spelling or don't capitalize your choices?")
#p1 as paper
elif p1 == "paper":
	if p2 == "rock":
		print("Paper covers rock; " + p1_name + " wins!")
	elif p2 == "scissors":
		print("Scissors cuts paper; " + p2_name + " wins!")
	else:
		print(p2_name + "- Something went wrong; Maybe check spelling or don't capitalize your choices?")
#p1 as scissors
elif p1 == "scissors":
	if p2 == "rock":
		print("Rock crushes scissors; " + p2_name + " wins!")
	elif p2 == "paper":
		print("Scissors cuts paper; " + p1_name + " wins!")
	else:
		print(p2_name + "- Something went wrong; Maybe check spelling or don't capitalize your choices?")
#Acccounting for typos or other wildcards
else:
	print("- Something went wrong; Maybe check spelling or don't capitalize your choices?")
