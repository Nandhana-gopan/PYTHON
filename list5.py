#smallest element
l=input().split()
smallest=int(l[0])
for i in range(1,len(l)):
    current=int(l[i])
    if current<smallest:
        smallest=current
print(smallest)