#input any 10 numbers find the first biggest and second biggest number
big1=0
big2=0
for x in range(1,11):
    no1=int(input("Enter number:"))
    if big1<no1:
        if big2<no1:
            big2=big1
            big1=no1
print(big1,"is a 1st big number")
print(big2,"is a 2nd big number")