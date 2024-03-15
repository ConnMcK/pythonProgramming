age=int(input("How old are you? - "))

if age>17:
    print("You are old enough to vote")
    registered=input("Are you registered to vote? (Yes/No) - ")
    if registered == "Yes":
        print("Great, your local polling station is the primary school")
    else:
        print("You can register to vote by contacting the council")
else:
    print("You are not old enough to vote")