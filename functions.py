# def printhello():
#     print("hello world")

# printhello()

# def add(n1, n2):
#     sum=n1+n2
#     return sum
# positional arguments
# print("the sum is",add(2,3))

# keyword argument
# print("the sum is ",add(n2=2,n1=3))

# default argument is:
# passing only one value

# arbitary arguments
# def addallnumbers(*args):
#     sum = 0
#     for i in args:
#         sum += i  
#     return sum  

# output = addallnumbers(2, 2, 3, 4)
# print("The sum is", output)


# dictionary arguments
# def studentinfo(**kwargs):
#     for x,y in kwargs.items():
#         print(x,"is",y)
# studentinfo(name="aaqib",age=21,city="karachi")
# studentinfo(name="ahmed",age=22,city="lahore")

# student_1= [70,80,90]
# sumof_marks= sum(student_1)
# total_sub=len(student_1)
# average= sumof_marks / total_sub
# print("average of student is ",average)

# defining functions
# def function_name(par1,par2,):
#         function statement
# """"""
def sum (a,b):
    c=a + b
    print("sum is",c )
sum(12,14)