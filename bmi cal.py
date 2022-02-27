print("Welcome to BMI Calculator")
a=float(input("Enter your height in Meters:"))
b=int(input("Enter your wieght in KGs:"))
c=round(b/(a*a),2)
print(f"Your BMI is {c} ")

if c <=18.5:
    print("You are underweight")
elif c <25:
    print("You are Normal")
elif c <30:
    print(f"You are Overweight")
else: 
    print("You are obese")