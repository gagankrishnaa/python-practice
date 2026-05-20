class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        
    def introduce(self):
        print(f"Hi, I'm {self.name} and my grade is {self.grade}")
        
    def is_passing(self):
        return self.grade >= 50
    
s1 = Student("Gagan" , 75)
s2 = Student("Rahul", 40)
s3 = Student("Prajwal", 60)

s1.introduce()
s2.introduce()
s3.introduce()

print(s1.is_passing())
print(s2.is_passing())
print(s3.is_passing())