import random
computer=random.choice([-1,0,1])
youstr=input("Choose between snake, water and gun")
youdict={"snake": -1,"water": 0,"gun": 1}
if (youstr not in youdict):
    print("Invalid input. Try snake, water, or gun.")
    exit()
reversedict={-1: "snake",0: "water",1: "gun"}
you=youdict[youstr]
print(f"computer chose {reversedict[computer]}")
if(computer==you):
    print("Its a draw")
elif(computer==-1 and you==0):
    print("computer wins")
elif(computer==-1 and you==1):
    print("you win")
elif(computer==0 and you==-1):
    print("you win")
elif(computer==0 and you==1):
    print("computer wins")
elif(computer==1 and you==0):
    print("you win")
elif(computer==1 and you==-1):
    print("computer wins")