print("welcome to the savings calulator")
varSalary = int(input("What is your monthly income after tax? - £"))
varCosts = int(input("What is your average monthly spending? - £"))
varTarget = int(input("What is your target savings amount? - £"))

varSavings = varSalary - varCosts

if varSavings < 0:
  print("You need to either earn more, or start spending less!")
  exit()

if varSavings>varTarget:
  print("Great news! Your target is acheivable")
else:
  print("You won't quite be able to reach your monthly target")

print(f"The most you can save each month is {varSavings}")