n1 = int(input("Enter the number N1:"))
n2 = int(input("Enter the number N2:"))
try:
    div = n1/n2
    print("Results of Div:",div)
except ZeroDivisionError as e:
    print("You are trying to dividing the number by zero")
    print("e value:",e)
print("End")