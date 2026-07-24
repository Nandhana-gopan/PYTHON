def is_prime(n):
    if n<=1:
        print("not prime")
    else:
     prime=True
     for i in range(2,n//2+1):#edge cases like 4 fails 
        if n%i==0:
           prime=False
           break
     if(prime):
       print("prime number")
     else:
       print("not prime")

num=int(input("enter a number:"))
is_prime(num)