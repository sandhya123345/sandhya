emp=input("Enter name:")
sal=float(input("Enter salary:"))
desi=input("Enter designation:")
bonus=0
if desi=="Manager":
    bonus==20*(sal/100)
    sal=sal+bonus
elif desi=="Analyst":
    bonus=10*(sal/100)
elif desi=="clerk":
    bonus=5*(sal/100)
    sal=sal+bonus
else:
    print("invalid designation entered")
print("Total salary is:",sal)
