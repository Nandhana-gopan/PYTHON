s=input()
rev=s[::-1]
print(rev)
if rev==s:
    print("is palindrome")
else:
    print("not palindrome")
v=input("enter the string:")
reverse=""
for i in range(len(v)-1,-1,-1):
    reverse=reverse+v[i]
print(reverse)
