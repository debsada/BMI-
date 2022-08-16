# BMI-
Calculator that calculates the Body Mass Index of a user and interprets its information 


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))



bmi = round(weight / (height ** 2)) #calculates the BMI and rounds it to nearest integer 

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi <= 35:
    print (f"Your BMI is {bmi}, you are obese")
else: 
    print (f"Your BMI is {bmi}, you are clincially obese")
