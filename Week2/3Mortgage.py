#I need to find out the user's age, wage, debt, deposit, and how expensive the house they want to buy

print("Hi. welcome to the online mortgage calculator. I will calulcate if a home is within your budget")
varAge=int(input("How old are you? - "))
#I am hopin the user does not use commas
varWage=int(input("What is your annual wage? - £"))
varDebt=int(input("How much debt do you have? - £"))
varDeposit=int(input("How much do you have to deposit? - £"))
varHouse=int(input("How much is the house you want to buy? - £"))


if varAge < 18:
  print("You are too young to buy a house")
  exit()
if varAge > 65:
  print("You are too old for a mortage")
  exit()

if varWage < 20000:
  print("You need to ern at least £20,000 a year to qualify for a mortgage")
  exit()

if varDeposit < (varHouse*0.1):
  print("You need to deposit at least 10% of the house price")
  exit()

varMaxHousePrice = (varWage*5) + varDeposit - varDebt
print(f"The maximum amount you can spend on a house is £{varMaxHousePrice}")

if varHouse > varMaxHousePrice:
  print("You cannot afford this house")
else:
  print("You can afford this house")