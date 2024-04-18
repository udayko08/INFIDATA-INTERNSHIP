l1 = [ 2,3,4,5,6]
print("List l1 is:",l1)
try:
    print("l1[2]:",l1[2])
    print("l1[3]:",l1[3])
    print("l1[6]:",l1[6])
except IndexError as e:
    print("u r trying to excess the wrong index")
    print(" e valus:",e)

print("end")