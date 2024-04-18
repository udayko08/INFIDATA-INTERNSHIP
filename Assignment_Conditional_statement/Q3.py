name =input("enter a candidate name:")
customer_id =input("Enter id:")
units =int(input("enter a consumed unite:"))
print("\nCustomer Name:",name)
print("\nCustomer Id:",customer_id)
print("\nElectricity bill:For Unites",(units))
if units <= 100:
    bill = 0
    print("No need to pay bill",bill)
elif units >= 100:
    bill=(units-100)*5
    print("The Required Rs",bill)
elif units >200:
    bill=(units-200)*10 +100*5
    print("The Required Rs",bill)
else:
    print("Invalid input")