import random
str=""
str1=""
str2=""
str3=""
shuffeled=[]
password=""
print("Welcome to password generatotr!!!!!!!!")
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['~','#','$','%','&','*']
n=int(input("how many numbers?"))
a=int(input("how many alphabets?"))
s=int(input("how many symbols?"))
for i in range(n):
    str1+=random.choice(numbers)
for i in range(a):
    str2+=random.choice(letters)
for i in range(s):
    str3+=random.choice(symbols)
str=str1+str2+str3
print(str)
for ele in str:
    shuffeled.append(ele)
random.shuffle(shuffeled)
finalstring=""
for i in shuffeled:
    finalstring+=i
print(finalstring)
    