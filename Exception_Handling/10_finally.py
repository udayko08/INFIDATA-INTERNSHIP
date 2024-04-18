l1 = [6,7,8,9]
print("List l1 is:",l1)
try:
    print("l1[2]:",l1[2])
    print("l1[3]:",l1[3])
except IndexError as e:
    print(" u r trying to acesss the wrong index")
    print("e values:",e)
except ZeroDivisionError as e:
    print(" u r trying divide an int num by zero")
    print("e value:",e)
finally:
    print("am at finally block:")
    print("Exceuting at finally:")
print("End")