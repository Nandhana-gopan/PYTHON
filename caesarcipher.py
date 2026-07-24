letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encryption(t,s):
    cipher_text=""

    for char in t:
        if char in letter:
          pos=letter.index(char)
          new_pos=(pos+s)%26
          cipher_text+=letter[new_pos]
        else:
           cipher_text+=char
    print(f"here is your encrypted code:{cipher_text}")
def decryption(dt,ds):
    decrypted_text=""
    for char in dt:
        if char in letter:
          pos=letter.index(char)
          new_pos=(pos-ds)%26
          decrypted_text+=letter[new_pos]
        else:
           decrypted_text+=char
    print(f"your decrypted mesg is {decrypted_text}")
          
to_exit=False
while(not to_exit):
    choice=input("Type encrypt or decrypt")
    text=input("enter your message").lower()
    shift=int(input("enter the shift number:"))
    if choice=="encrypt":
      encryption(t=text,s=shift)
    elif choice=="decrypt":
      decryption(text,shift)
    cont=input("yes to continue no to exit")
    if cont=="no":
      to_exit=True
      print("gudbye")