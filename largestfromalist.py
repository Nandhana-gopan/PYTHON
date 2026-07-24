numbers=input().split(",")
max=0
for i in numbers:
    if int(i)>max:
        max=int(i)
print(f"{max} is the largest number")