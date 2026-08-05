# def recursion():
#     print(1)
#     recursion()
# recursion()



# def printing():#each and everyutime a ufnction calls it start executing from the beginning(everytime count becomes 0)
#     count=0
#     if count==4:
#         return
#     print(count)
#     count=count+1
#     printing()
# printing()


def printing(count):          #each time the previous count value is passed to the next fn call
    if count==4:
        return
    print(count)
    count=count+1
    printing(count)
printing(0)