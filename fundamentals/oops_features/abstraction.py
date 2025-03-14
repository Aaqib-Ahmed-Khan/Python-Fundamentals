# hiding unnecesary details from users using class and methods

class Student:
   def __init__(self,name,grade,percentage):  #method
    self.name=name    #attribute
    self.grade=grade     #attribute
    self.percentage=percentage

   def student_details(self):
     print(f"{self.name} is in class {self.grade},with {self.percentage+2}%") #hidden from users the increased algorithm percentage  

# object -instance of c  lass
student1=Student("AAQIB",11,96)
print(student1.name,student1.grade,student1.percentage)

student2=Student("ahmed",1,97)
print(student2.name,student2.grade,student2.percentage)

student1.student_details()
student2.student_details()