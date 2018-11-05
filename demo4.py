name=input("Enter name:")
stype=input("Enter slab type:")
units=int(input("Enter units:"))
bill=0
if stype=="industry":
    bill==units*5.25
    print("Total bill:",bill)
elif stype=="commercial":
    bill==units*4
    print("Total bill:",bill)
elif stype=="residence":
    bill=units*3.80
    print("Total bill:",bill)
