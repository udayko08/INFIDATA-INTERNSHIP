n1 = int(input("enter the Number:"))
n2 = int(input("enter the number:"))
ch=int(input("enter your choice 1:Add, 2:Sub, 3:Mul, 4:Div, 5:Mod:"))
if(ch==1):
    res=n1+n2
    print("Add of {0} and {1} is {2}".format(n1,n2,res))
elif(ch==2):
    res=n1-n2
    print("Sub of {0} and {1} is {2}".format(n1,n2,res))
elif(ch==3):
    res=n1*n2
    print("Mul of {0} and {1} is {2}".format(n1,n2,res))
elif(ch==4):
    res=n1/n2
    print("Div of {0} and {1} is {2}".format(n1,n2,res))
elif(ch==5):
    res=n1%n2
    print("Mod of {0} and {1} is {2}".format(n1,n2,res))
else:
    print("invalid choice")