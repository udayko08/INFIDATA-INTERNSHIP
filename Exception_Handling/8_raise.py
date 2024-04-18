print("raise keyword demo")
try:
    raise ZeroDivisionError("Demo Message")   #raise is used for to give explict call to except block
except ZeroDivisionError as e:
    print(" am at ZeroDivisionError block")
    print("e values:",e)
print("end")