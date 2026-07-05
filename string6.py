#count frequency of each character
word=input("enter a string:")
printed=""
for i in word:
    if i not in printed and not i.isspace():
        print("count of:",i,word.count(i))
        printed+=i