print("Rock...")
print("Paper...")
print("Scissors...")

print("Please enter name for Player 1: ")
p1_name = input()

print("Please enter name for Player 2: ")
p2_name = input()

p1 = input("Player 1, make your move. Choose 'rock', 'paper', or 'scissors': \n")
p2 = input("Player 2, make your move. Choose 'rock', 'paper', or 'scissors': \n")

#Player 1 options
#p1 as rock
if p1 == p2:
	print("Tie Game. Try again!")
elif p1 == "rock" and p2 == "paper":
	print("Paper covers rock; " + p2_name + " wins!")
elif p1 == "rock" and p2 == "scissors":
	print("Rock crushes scissors; " + p1_name + " wins!")
#p1 as paper	
elif p1 == "paper" and p2 == "rock":
	print("Paper covers rock; " + p1_name + " wins!")
elif p1 == "paper" and p2 == "scissors":
	print("Scissors cuts paper; " + p2_name + " wins!")
#p1 as scissors
elif p1 == "scissors" and p2 == "rock":
	print("Rock crushes scissors; " + p2_name + " wins!")
elif p1 == "scissors" and p2 == "paper":
	print("Scissors cuts paper; " + p1_name + " wins!")
#counting for typos or other wildcards
else:
	print("Something went wrong; Maybe check spelling or don't capitalize your choices?")
