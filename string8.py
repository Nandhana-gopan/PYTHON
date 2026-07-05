#remove duplicate characters
word=input("enter the string:")
printed=""
for i in word:
    if i not in printed:
        printed+=i
print(printed)