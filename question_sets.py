l1=[1,4,5]
l2=[3,5,1]
l3=[5,1,7]

# type casting
s1=set(l1)
s2=set(l2)
s3=set(l3)
s1s2=s1.intersection(s2)
final_set=s1s2.intersection(s3)
final_list=list(final_set)
print(final_list)
