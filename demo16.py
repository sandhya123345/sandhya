#input any 10 numbers find out the no of positive numers and no of negative numbers
posno=0
negno=0
for x in range(1,11):
    no=int(input("enter number:"))
    if no>=1:
        posno+=1
    else:
        negno+=1
print("no of +ve numbers: ",posno)
print("no of -ve numbers: ",negno)
