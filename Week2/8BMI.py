print("Welcome to the BMI calulator")
varHeight = float(input("Enter your height in m - "))
varWeight = float(input("Enter your weight in kg - "))

BMI = varWeight / (varHeight * varHeight)
print("Your BMI is " + str(BMI))

if BMI < 18.5:
  print("You are underweight")
elif BMI < 25:
  print("You are normal weight")
elif BMI < 30:
  print("You are overweight")
else;
  print("You are obese")


