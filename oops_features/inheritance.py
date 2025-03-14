#allows the class(child) to resue the props and methods of another child (parent)

# this is parent class 
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


# child class
class graduate(Student):
   def _init_(name,grade):
     super().__init__(name,grade)