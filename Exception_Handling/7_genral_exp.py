n1 = int(input("Enter the number N1:"))
n2 = int(input("Enter the number N2:"))
l1 =[ 4,5,6,7,8]
print("List l1 is:",l1)
try:
    div=n1/n2
    print("Results of div:",div)
    print("l1[[2]:",l1[2])
    print("l1[5]:",l1[5])
except ZeroDivisionError as e:
    print(" u r trying divide an int num by zero")
    print("e value:",e)
except IndexError as e:
    print(" u r trying to acesss the wrong index")
    print("e values:",e)
except Exception as e:
    print("Am at Generalized except block")
    print("e valus:",e)
print("End")