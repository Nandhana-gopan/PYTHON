def NtoOne(i,n):
    if i<1:#base case
        return
    print(i)
    NtoOne(i-1,n)
n=int(input())
NtoOne(n,n)