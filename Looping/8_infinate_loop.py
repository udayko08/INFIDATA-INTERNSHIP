l = int(input("Enter Length:"))
b = int(input("Enter Breath:"))
h= int(input("Enter height:"))
while(True):
    choice = int(input("Enter your choice 1:Area,2:Volume,3:Exit:\n"))
    if choice==1:
        area = l*b
        print("Are of Rectangle is:",area)
    elif choice==2:
        volume = l*b*h
        print("Volume of Rectangle is:",volume)
    elif choice==3:
        exit(0)
    else:
        print("Invalid choice")