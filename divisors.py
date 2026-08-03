import math
numlist=[]
def divisors(n):
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            numlist.append(i)
            #print(i, " ",end="")
            if n/i!=i:
                numlist.append(n//i)
                #print(n//i," ",end="")
    numlist.sort()
    print(numlist)
num=int(input())
divisors(num)