import random

computerChoice=["rock","paper","scissors"]
userChoice=input("Choose rock/paper/scissors - ")
if userChoice.lower() == "rock":
    print("You have chosen rock!")
elif userChoice.lower() == "paper":
    print("You have chosen paper!")
elif userChoice.lower() == "scissors":
    print("you have chosen scissors!")
else:
    print("Your choice makes no sense")

#sort out the lower issue

computerChoice = random.choice(computerChoice)
print(f"The computer chooses {computerChoice}!")

if userChoice not in computerChoice:
    print("You are a loser")
elif userChoice == "rock" and computerChoice == "rock":
    print("It is a draw")
elif userChoice == "rock" and computerChoice == "paper"