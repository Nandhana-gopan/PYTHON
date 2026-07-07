#largest element without using max fn
l=input().split()
largest=int(l[0])
for i in range(1,len(l)):
    current=int(l[i])
    if current>largest:
        largest=current
print(largest)

