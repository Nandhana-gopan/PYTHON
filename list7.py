#Reverse a list without using: reverse()   [::-1]
l=input().split()
for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")