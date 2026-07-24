import math
def wallarea(h,w,c=7):
    numcans=math.ceil((h*w)/c)
    print(numcans)
height=float(input("enter the height of the wall:"))
width=float(input("enter the width of the wall:"))
wallarea(height,width)