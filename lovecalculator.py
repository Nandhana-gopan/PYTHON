p1=input("enter your name:")
p2=input("enter your paartner name:")
fullname=p1+p2
inlower=fullname.lower()
t=inlower.count('t')
r=inlower.count('r')
u=inlower.count('u')
e=inlower.count('e')
total_true=t+r+u+e
l=inlower.count('l')
o=inlower.count('o')
v=inlower.count('v')
e=inlower.count('e')
total_love=l+o+v+e

total_score=str(total_true)+str(total_love)
if int(total_score)>90:
    print(f"your love score is {total_score}.Soulmates!!!!")
elif int(total_score)<10:
    print(f"Your love score is {total_score}.Think about it!!!")
else:
    print(f"Your love score is {total_score}.You guys are alright")