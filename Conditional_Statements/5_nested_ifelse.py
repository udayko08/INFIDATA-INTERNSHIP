print("select a food category 1: veg, 2:non_veg:")
choice=int(input())
if(choice==1):
    print("You have selected veg category:")
    menu=int(input("select menu 1:meals 2:Dosa 3:idli:"))
    if(menu==1):
        print("you have selected meals:")
    elif(menu==2):
        print("you have selected Dosa:")

elif(choice==2):
    print("you have selected non_veg:")
    menu=int(input("select menu 4:chickken_curry 5:hot_wings:"))
    if(menu==4):
        print("you have selected chickken curry:")
    elif(menu==5):
        print("you have selected hot wings:")
    else:
        print("invalid choice:")
else:
        print("invalid category:")