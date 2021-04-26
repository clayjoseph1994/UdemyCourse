#This is the fourth iteration of the automated version of RPS where a user battles a "computer"
#opponent in a game. I added functions in this refactor job to make things a little cleaner. The variable winning_score
#determines the amount of wins necessary by the computer or player to exit the program. You can change the value of this
#variable to determine how long the game goes
from random import randint

game = 0
player_wins = 0
comp_wins = 0
winning_score = 2
p1_name = ""


def intro():
    print("You are playing a game of rock, paper, scissors with a computer opponent")
    print("First to win %s battles wins the game!\n" % winning_score)
    print("Rock...\nPaper...\nScissors...\nSHOOT!\n")


def gameloop():
    global player_wins
    global comp_wins
    global game
    global p1_name

    p1_name = input("Please enter your name: ")
    while p1_name == "":
        p1_name = input("No name detected. Please enter your name, or a fake one (give me something to work with here xD): ")

    #adding loop to allow 3 plays (best 2/3)
    while player_wins < winning_score and comp_wins < winning_score:
        comp = randint(0, 2)
        game += 1
        print("*" * 80)
        game_num = "Battle: " + str(game)
        print(game_num)

        p1 = input(p1_name + ", please make your move. Choose 'rock', 'paper', or 'scissors': ").lower()
        if p1 == "quit" or p1 == "q":
            print("\n+---------------------------------+")
            print(f"| Your Score: {player_wins} Computer Score: {comp_wins} |")
            print("+---------------------------------+")
            break
        print()
        #For Computer random play
        #0 = rock
        #1 = paper
        #2 = scissors

        #If computer chooses rock
        if comp == 0:
            if p1 == "rock":
                print("The computer also chose rock.")
                print("It's a tie!")
            elif p1 == "paper":
                print("The computer chose rock.")
                print("Paper covers rock; " + p1_name + " wins!")
                player_wins += 1
            elif p1 == "scissors":
                print("The computer chose rock.")
                print("Rock crushes scissors; Better luck next time!")
                comp_wins += 1
            elif p1 == "":
                print("You didn't make a choice! Please play again and choose one of the 3 options.")
            else:
                print("- Something went wrong; Maybe check spelling?")
        #If computer chooses paper
        elif comp == 1:
            if p1 == "paper":
                print("The computer also chose paper.")
                print("It's a tie!")
            elif p1 == "rock":
                print("The computer chose paper.")
                print("Paper covers rock; Better luck next time!")
                comp_wins += 1
            elif p1 == "scissors":
                print("The computer chose paper.")
                print("Scissors cuts paper; " + p1_name + " wins!")
                player_wins += 1
            elif p1 == "":
                print("You didn't make a choice! Please play again and choose one of the 3 options.")
            else:
                print("- Something went wrong; Maybe check spelling?")
        #If computer chooses scissors
        elif comp == 2:
            if p1 == "scissors":
                print("The computer also chose scissors.")
                print("It's a tie!")
            elif p1 == "rock":
                print("The computer chose scissors.")
                print("Rock crushes scissors; " + p1_name + " wins!")
                player_wins += 1
            elif p1 == "paper":
                print("The computer chose scissors.")
                print("Scissors cuts paper; Better luck next time!")
                comp_wins += 1
            elif p1 == "":
                print("You didn't make a choice! Please play again and choose one of the 3 options.")
            else:
                print("- Something went wrong; Maybe check spelling?\n\n")
        print("\n+---------------------------------+")
        print(f"| Your Score: {player_wins} Computer Score: {comp_wins} |")
        print("+---------------------------------+")


def end():
    global p1_name
    global player_wins
    global comp_wins

    if player_wins > comp_wins:
        print("\n\n*******************************************************************************")
        print("!!!!!!!!!!!!!!!!!!!!!!! " + p1_name.upper() + " WINS THE GAME !!!!!!!!!!!!!!!!!!!!!!!")
    elif player_wins < comp_wins:
        print("\n\n*******************************************************************************")
        print("!!!!!!!!!!!!!!! THE COMPUTER WINS THE GAME. TRY AGAIN !!!!!!!!!!!!!!!")
    else:
        print("\n\n*******************************************************************************")
        print("!!!!!!!!!!!!!!! IT'S A TIE !!!!!!!!!!!!!!!")


if __name__ == '__main__':
    intro()
    gameloop()
    end()
