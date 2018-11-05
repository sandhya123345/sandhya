#input any four digit number and  find out the sum of digits
no=int(input("enter no:"))
sum=0
while no!=0:
    r=no%10
    no=no//10
    sum=sum+r
print("Sum of digits:",sum)