# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Welcome to Pizza Order Portal")
bill=0 #Declaired the bill as 0


#Taken the inpiut for all the options 
a=(input("Please confirm the size of Pizza? S,M,L \n"))
o=(input("Do you need onion toppings? Y/N \n"))
c=(input("Do you need cheese on it? Y/N\n"))
if a=="s":
    #increased the value of the bill 
    bill+=15
    
elif a=="m":
    bill+=25
    
else:
    bill+=45
    
if o=="y":
    if a=="s":
        bill+=2
    else:
        bill+=3
        
if c=="y":
    bill+=1
    
    
print(f'Your final bill is $ {bill}')