# using oops creating student records
# class-blueprint or template
# class Student:
#     name="aaqib"
#     grade=10



# object -instance of class
# student1=Student()
# print (student1.name,student1.grade)

# student2=Student()
# print (student2.name,student2.grade)


# functuon in class is called method
# __init__method-constructor-value initialize-fix
# self parameter-reference or connection build btw class or object 
# class and object fix
# first method always write with init

class Student:
   def __init__(self,name,grade):  #method
    self.name=name    #attribute
    self.grade=grade     #attribute

   def student_details(self):
     print(f"{self.name} is in class {self.grade}")

# object -instance of class
student1=Student("AAQIB",11)
print(student1.name,student1.grade)

student2=Student("ahmed",1)
print(student2.name,student2.grade)

student1.student_details()
student2.student_details()