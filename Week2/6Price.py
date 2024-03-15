print("Welcome to the price calulator")
varBase =float(input("What is the ase price of the product? - £"))
varTax = float(input("What is the sales tax in you area?(as decimal) - "))
varShipping = float(input("What is the shipping cost? - £"))


varGross = varBase + (varBase * varTax) + varShipping
if varGross > 100:
  varGross = varGross * 0.9
  print("We have given you a ten percent discount")


print(f"Your total is £{varGross}")