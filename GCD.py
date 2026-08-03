# firstnum=int(input("enter the first number:"))
# secnum=int(input("enter the sec num:"))
# for i in range(1,min(firstnum,secnum)+1):       -------> Bruteforce
#     if(firstnum%i==0 and secnum%i==0):
#         gcd=i
# print(gcd)
a=int(input())
b=int(input())
while b!=0:
    temp1=b               #---------->Optimization
    temp2=a%b
    a=temp1
    b=temp2
print(a)