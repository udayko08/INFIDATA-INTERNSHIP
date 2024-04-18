present = int(input("Enter the Number Working days the student attend:"))
absent = int(input("Enter the no of days the student is absent:"))
p = (present-absent)/present*100
print("The total no Precentage the Student Attend the class:",p)
if p>75:
    print("The student can write a exam")
else:
    print("You cannot attend the exam")
