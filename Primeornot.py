# import math
# def primeornot(n):
#     count=0
#     for i in range(1,int(math.sqrt(n))+1):
#         if n%i==0:
#             count+=1
#             if(n/i!=i):                    #optimal
#                 count=count+1
#     if count==2:
#         print("prime")
#     else:
#         print("not prime")
# n=int(input())
# primeornot(n)

def primeornot(n):
    for i in range(2,n//2):
        if(n%i==0):
            print("not prime")
            return
    print("prime")
n=int(input())
primeornot(n)
