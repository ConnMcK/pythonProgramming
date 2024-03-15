#This should be simpler than the mortgage calulator

print("Hello. Welcome to the grade calculator.")
varScore = int(input("Please enter the student's score - "))


if varScore >= 90:
  print("They scored an A")
elif varScore >= 80:
  print("They scored a B")
elif varScore >= 70:
  print("They scored a C")
elif varScore >= 60:
  print("They scored a D") 
else:
  print("They scored an F")