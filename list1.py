grocery=[]
grocery.append("vegetables")
grocery.append("fruits")
grocery.append("milk")
print(grocery)
print(grocery[0])
print(grocery[-1])
print(len(grocery))
for item in grocery:
    print(item)
for i in range(len(grocery)):
    print(i,grocery[i])
grocery[2]="butter"
print(grocery)
