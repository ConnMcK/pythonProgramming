import random

computerChoice=["rock","paper","scissors"]
userChoice=input("Choose rock/paper/scissors - ").lower()
if userChoice == "rock":
    print("You have chosen rock!")
elif userChoice == "paper":
    print("You have chosen paper!")
elif userChoice == "scissors":
    print("you have chosen scissors!")
else:
    print("Your choice makes no sense")
    print("Your are a loser!")


computerChoice = random.choice(computerChoice)
print(f"The computer chooses {computerChoice}!")

if userChoice == computerChoice:
    print("It is a draw")
elif userChoice == "rock" and computerChoice == "scissors":
    print("You win!")
elif userChoice == "paper" and computerChoice == "rock":
     print("You win!")
elif userChoice == "scissors" and computerChoice == "paper":
     print("You win!")
else:
     print("You lose!")