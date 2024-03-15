username=input("Please enter your username - ")
password=input("Please enter your password - ")
userTitle=input("Please enter your title - ")
fullName=input("Please enter you full name - ")
age=input("Please enter your age - ")
email=input("Please enter your email address - ")

fullName=fullName.title()
userTitle=userTitle.upper()
passDigit=password.isdigit()
ageDigit=age.isdigit()
email=email.lower()

print(f"Your fullname is {userTitle} {fullName}")
if passDigit:
    print("Your password is a digit")
else:
    print("Your password is not a digit")
if ageDigit:
    print("Your age is a digit")
else:
    print("Your age is not a digit")
print(f"Your email address is {email}")