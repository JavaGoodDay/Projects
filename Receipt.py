prod=input("enter Product:")
pri=input("enter Price:")
qty=input("enter Quantity:")

amt=float(pri)*int(qty)

vat=amt*15/100

bill=amt+vat

print("Receipt")
print()
print(prod,"_____""£",pri)       
print("Quantity",qty)
print()
print()
print("Bill")                     
print("£",bill)
print()
print("VAT")                      
print("£",vat)