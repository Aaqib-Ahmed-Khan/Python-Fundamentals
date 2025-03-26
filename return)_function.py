# def multi(a, b):
#     c = a * b
#     return "Product is", c  # Returns a tuple

# result = multi(10, 20)
# print(result) 

# local  variable /global var
# def xyz(a,b):
#     a=10
#     b=20
#     c=a*b
#     return c
# x=xyz(10,20)
# print (x)

def odd_or_even():
    num=int(input("enter n: "))
    if num%2==0:
        print("even")
    else:
        print("odd")
    return num
user=odd_or_even()
print(user)