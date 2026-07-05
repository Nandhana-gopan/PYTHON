#print characters of a string (in reverse order as well)
word=input("enter the string:")
length=len(word)
for i in range(0,length):
    print(word[i])
print("In reverse:")
for j in range(length-1,-1,-1):
    print(word[j])