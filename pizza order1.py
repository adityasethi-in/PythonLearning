# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Welcome to Pizza Order Portal")
a=str(input("Please confirm the size of Pizza? S,M,L \n"))
if a=="s":
    o=str(input("Do you need onion as topping ?Y/N\n "))
    if o=="y":
        c=str(input("Do you need Extra Cheese ?Y/N\n "))
        if c=="y":
            print("Your bill is 75$ ")
        else :
            print("Your bill is 50$")
    else:
        print("Your bill is 45$")
if a=="m":
    o=str(input("Do you need onion as topping ?Y/N\n"))
    if o=="y":
        c=str(input("Do you need Extra Cheese ?Y/N\n"))
        if c=="y":
            print("Your bill is 55$ ")
        else :
            print("Your bill is 60$")
    else:
        print("Your bill is 53$")

if a=="l":
    o=str(input("Do you need onion as topping ?Y/N\n"))
    if o=="y":
        c=str(input("Do you need Extra Cheese ?Y/N\n"))
        if c=="y":
            print("Your bill is 92$ ")
        else :
            print("Your bill is 100$")
    else:
        print("Your bill is 89$")   

