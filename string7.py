word=input("enter a string:")
new=""
for i in word:
    if not i.isspace():
        new=new+i
print(new)