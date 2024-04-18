student_name = input("Enter the Student Name:")
student_reg = input("Enter the Student Register No:")
grade =int(input("Enter the Percentage:"))
print("\nThe Student Name is:",student_name)
print("\nThe Student Register No is:",student_reg)
print("\nThe Student Percentage is:",grade)
if grade >90 and grade <=100:
    print("The Grade is A")
elif grade >80 and grade <=90:
    print("The Grade is B")
elif grade >=60 and grade <=80:
    print("The Grade is C")
elif grade <60:
    print("The Grade is D")
else:
    print("Invalid Grade")