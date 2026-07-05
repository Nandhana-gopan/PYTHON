#count uppercase and lowercase letters and count numbers
word=input()
ucount=0
lcount=0
ncount=0
scount=0
for i in word:
    if i.isupper():
        ucount+=1
    elif i.islower():
        lcount+=1
    elif i.isnumeric():
        ncount+=1
    elif i.isspace():
        scount+=1

print(f"uppercase:{ucount}\nlowercase:{lcount}\nnumbers:{ncount}\nspaces:{scount}")
