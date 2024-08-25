class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)

s1 = Student(22, 35)
s2 = Student(35, 45)
s3 = Student(23, 55)
s4 = s1 + s2 + s3

print(s4.m1, s4.m2) 
