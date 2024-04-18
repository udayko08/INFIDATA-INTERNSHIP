age = int(input("Enter the Age:"))
gender = input("Enter gender (M/F):").upper()
days = int(input("Enter the No of Days:"))
if age >= 18 and age <= 40:
    if gender == 'M':
        if age < 30:
            wages = days*700
            print("The wages If Age is less then 30 age:",wages)
        else:
            wages = 800*days
            print("The wages If Age is greater  then 30 age:", wages)
    elif gender == 'F':
        if age < 30:
            wages = 750*days
            print("The wages If Age is less then 30 age:", wages)
        else:
           wages = 850*days
        print("The wages If Age is less then 30 age:",wages)
else:
        print("invalid input")