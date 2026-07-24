list1=[1,1,1]
list2=[1,1,1]
list3=[1,1,1]
matrix=[list1,list2,list3]
print("\n",list1,"\n",list2,"\n",list3)
position=input("enter the position:")
row_no=int(position[0])
col_no=int(position[1])
matrix[row_no-1][col_no-1]="X"
print("\n",list1,"\n",list2,"\n",list3)



