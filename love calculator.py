print("Love Calculator")
name1=input("What is your name\n")
name2=input("What is your partner's name\n")
combine_strings=name1+name2
la=combine_strings.lower()
t=la.count("t")
r=la.count("r")
u=la.count("u")
e=la.count("e")
true=t+r+u+e
l=la.count("l")
o=la.count("o")
v=la.count("v")
e=la.count("e")
love=l+o+v+e
ls=int(str(true)+str(love))
print(f"your love % is {ls}")

if (ls < 10) or (ls > 90):
    print("You are like coke and mitos")
elif ls>=40 and ls<=50:
    print("You are alright together")
else:
    print(f"Your score is {ls}")