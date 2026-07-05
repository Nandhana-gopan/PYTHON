#print the length of a string without using len function
word=input("enter the string:")
count=0
for i in word:
    count+=1
print(f"number of characters: {count}")