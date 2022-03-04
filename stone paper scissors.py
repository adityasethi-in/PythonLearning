import random
a=input("Lets play Stone, Paper and Scissors, Type your selection, i.e.,  Stone, Paper or Scissors\n")
a=a.lower()
game=["Stone", "Paper", "Scissors"]
i=random.choice(game)

print("Alright, Here is my response: "+(i))
if a=="stone" and i=="Stone":
    print("Try Again")
if a=="stone" and i=="Scissors":
    print("You won this round")
if a=="stone" and i=="Paper":
    print("I won")
    
if a=="paper" and i=="Paper":
    print("Try Again")
if a=="paper" and i=="Stone":
    print("You won this round")
if a=="paper" and i=="Scissors":
    print("I won")
    
if a=="scissors" and i=="Scissors":
    print("Try Again")
if a=="scissors" and i=="Paper":
    print("You won this round")
if a=="scissors" and i=="Stone":
    print("I won")

            
    
