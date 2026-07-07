l=input().split()
num=int(input("enter the number to search:"))
found=False
for i in range(0,len(l)):
    if(int(l[i])==num):
        found=True
        break
if(found):
    print("element found at index",i+1)
else:
    print("not found")