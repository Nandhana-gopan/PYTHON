#first non repeating character and first repeating charcter
word=input("enter the string:")
for ch in word:
    if(word.count(ch)==1):
        print("first non repeating char:",ch)
        break
for ch in word:
    if(word.count(ch)>1):
        print("first repeating charcter",ch)
        break
