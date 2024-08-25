

class Student:
    def __init__(self,name,age,**Computer_info) :
        self.name = name
        self.age = age
        self.lap = self.Computer(Computer_info.get('brand'),Computer_info.get('gen'))
    class Computer:
        def __init__(self,brand,gen) -> None:
            self.brand = brand 
            self.gen = gen 
            
s1 = Student("Aravind",23,brand="HP",gen=11)
s2 = Student("Naveen",23,brand="Dell",gen=10)

print(s1.lap.gen)

        