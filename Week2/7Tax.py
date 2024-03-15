print("Welcome to the tax calulator")
varIncome = int(input("What is your total annual household income? - £"))
varmarried = input("Are you married? (Y/N) - ").lower


varTax=float(0)
if varmarried == "n":
  if varIncome <= 9950:
    varTax = varIncome * 0.10
  elif varIncome <= 40525:
    varTax = 995 + ((varIncome - 9950) * 0.12)
  elif varIncome <= 86375:
    varTax = 4664 + ((varIncome - 40525) * 0.22)
  elif varIncome <= 164925:
    varTax = 14751 + ((varIncome - 86375) * 0.24)
  elif varIncome <= 209425:
    varTax = 33603 + ((varIncome - 164925) * 0.32)
  elif varIncome <= 523600:
    varTax = 47843 + ((varIncome - 209425) * 0.35)
  else:
    varTax = 157804 + ((varIncome - 523600) * 0.37)
else:
  if varIncome <= 19900:
    varTax = varIncome * 0.10
  elif varIncome <= 51050:
    varTax = 1990 + ((varIncome - 19900) * 0.12)
  elif varIncome <= 172750:
    varTax = 9328 + ((varIncome - 51050) * 0.22)
  elif varIncome <= 329850:
    varTax = 29502 + ((varIncome - 172750) * 0.24)
  elif varIncome <= 418850:
    varTax = 67206 + ((varIncome - 329850) * 0.32)
  elif varIncome <= 1047200:
    varTax = 95686 + ((varIncome - 418850) * 0.35)
  else:
    varTax = 315608 + ((varIncome - 1047200) * 0.37)

print(f"Your tax this year is £{varTax}")