def sumofN(i,n,total):
    if i>n:
        print(total)
        return
    total=total+i
    sumofN(i+1,n,total)
n=int(input())
sumofN(1,n,0)
