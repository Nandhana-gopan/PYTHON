#count of even and odd integers
l=input().split()
evencount=0
oddcount=0
for i in range(0,len(l)):
    current=int(l[i])
    if(current%2==0):
        evencount+=1
    else:
        oddcount+=1
print(f"even numbers count:{evencount}\nodd numbers count:{oddcount}")