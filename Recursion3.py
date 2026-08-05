# def OnetoN(N,count):
#     if count==N+1:#--------------->basecase
#         return
#     print(count,)
#     OnetoN(N,count+1)
# limit=int(input())
# OnetoN(limit,1)

def N(i,n):
    if i>n: #basecase
        return
    print(i)
    N(i+1,n)
N(1,6)