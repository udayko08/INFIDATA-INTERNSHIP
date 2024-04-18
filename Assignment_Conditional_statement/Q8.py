salary = float(input("Enter your salary:"))
services = int(input("Enter your years of services:"))
if services > 10:
    bonus1 = salary*0.10
    print("The salary + Bonus Is:",bonus1+salary)
elif services <=6 and services <= 10:
    bonus2 = salary*0.08
    print("The salary + Bonus Is:", bonus2+salary)
else:
    bonus3 = salary*0.05
    print("The salary + Bonus Is:",bonus3+salary)