
print("Welcome to the treasure hunt")

a=str(input("Do you want to take a left or a right\n")).lower()

if a=="left":
    b=str(input("Do you wanna swim or you wish to walk\n")).lower()
    
    if b=="swim":
        c=str(input("Which door do you wish to choose? Red/Yello?Green\n")).lower()
        if c=="Green":
            print("You won this game")
        else:
            print("Game over, not the correct door")
    else:
        print("Game over, tiger ate you")
        
       
else:
    print("Game Over, please try again, you fell in a well")
    
    