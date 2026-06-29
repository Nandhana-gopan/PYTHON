num=int(input("enter the number:"))
temp=num
rev=0
while temp!=0:
    digit=temp%10
    temp=temp//10
    rev=rev*10 + digit
print("reverse of  num is",rev)