price = float(input("Enter the cost price of the bike Rs:"))
tax = int(input("enter the tax Percentage:"))
if price>=100000:
    tax_prt = price*0.15
elif price>=50000 and price <100000:
    tax_prt = price * 0.10
elif price<50000:
    tax_prt = price*0.05
print("road tax to be paid:Rs",tax_prt)
print("The total Amount to be Paid by Customer is:",(price+tax_prt))