n=int(input("enter the range:"))
if(n<2):
        print("no prime numbers")
else:
     for num in range(2,n+1):
            is_prime=True
            for i in range(2,num):
                   if(num%i==0):
                          is_prime=False
                          break
            if(is_prime):
                   print(num)
#prime numbers between given range
# start=int(input("enter the starting range:"))
# end=int(input("enter the ending range:"))
# if(end<2):
#     print("no prime numbers in this range")
# else:
#     start=max(start,2)
#     for num in range(start,end+1):
#         is_prime=True
#         for i in range(2,num):
#             if(num%i==0):
#                 is_prime=False
#                 break
#         if(is_prime):
#             print(num)


     
            
