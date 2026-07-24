heights=input().split(",")
sum=0
count=0
for i in heights:
    sum=sum+float(i)
    count=count+1
avg=round(sum/count)
print(avg)
