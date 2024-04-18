num1 = int(input("Enter the First number:"))
num2 = int(input("Enter the Second number:"))
num3 = int(input("Enter the Thrid number:"))
print("The first number is:",num1)
print("The second number is:",num2)
print("The thrid number is:",num3)
if num1 > num2 and num1 > num3:
    print("Number 1 is the biggest:", num1)
elif num2 > num1 and num2 > num3:(
    print("Number 2 is the biggest:", num2))
elif num3 > num1 and num3 > num2:
        print("Number 3 is the biggest:", num3)
else:
    print("There is at least one tie for the biggest number.")