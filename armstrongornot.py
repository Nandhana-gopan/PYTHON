n=int(input())
temp=n
count=len(str(n))
total=0
while temp>0:
    digit=temp%10
    total+=digit**count
    temp=temp//10
if total==n:
    print("armstrong")
else:
    print("not armstrong")


