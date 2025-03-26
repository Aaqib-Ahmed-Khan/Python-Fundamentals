n=int(input("enter size of list"))
list=[]
for _ in range(n):
     num =int(input())

     list.append(num)
indx1= int(input("enter index:"))
indx2= int(input("enter indx2:"))
print(list)
#  swapping values at idx1 and idx2
temp = list[indx1]
list[indx1] = list[indx2]
list[indx2] = temp
print(list)