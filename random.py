
import random
a=input("Who will pay the bill? Let it be decided by the random name name selector.Give me all the names with a comma and then press enter.\n")
b=a.split(", ")
length=len(b)
i=random.randint(0, length-1)

print(b[i] + " is going to buy the meal")
