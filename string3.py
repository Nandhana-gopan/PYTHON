#count vowels and consonants
word=input()
vcount=0
ccount=0
vowels="AEIOUaeiou"
for i in word:
    if i in vowels:
        vcount+=1
    elif i.isalpha() and i not in vowels:
        ccount+=1
print(f"vowels count:{vcount}\nconsonents count:{ccount}")


