# dict={
#     'a':100,
#     'b':200,
#     'c':300
# }
# print("the sum of dictionary values is",sum(dict.values())) 

input_string=input("enter a string:")
n=int(input("enter n :"))
alphabets="abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dict1 = dict(zip(alphabets,reverse_alphabets))
prefix= input_string[0:n-1]
suffix= input_string[n-1:]
mirror=""
for i in range(0,len(suffix)):
    mirror=mirror + dict1[suffix[i]]

# creating a final string
res=prefix + mirror
print("the result is:",res)
