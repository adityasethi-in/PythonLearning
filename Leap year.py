print("Welcome to Leap year checker")
a=int(input("Enter the year that you wish to check : "))

if a % 4==0:
    if a % 100==0:
        if a % 400==0:
             print(f"This {a} is a leap year")
        else:
            print(f"{a} is not a leap year")
    else:   
        print(f"This year {a} is a leap year")
    
else:
    print("This is not a leap year")

        
