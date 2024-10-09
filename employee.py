class Person:
    
    def __init__(self,name,idnumber) :
        self.name = name
        self.idnumber = idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        
class Employee ( Person ):
    def __init__(self,name,idnumber,salary,post):
        self.salary  = salary
        self.post = post
        
        Person.__init__(self,name,idnumber)
        
a = Employee("Rahul",88789,20000,"Intern")

a.display()
print(f"{a.salary}")
print(f"{a.post}")