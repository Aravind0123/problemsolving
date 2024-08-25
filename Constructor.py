class Details:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def output(self):
        print(self.name,self.age)
    def compare(self,d2):
            try:
                if self.age == d2.age:
                    print("They are same")          
                else:
                    print("They are not Same")
            except Exception as e:
                print("Error")
d1 =Details("Aravind",23)
d2 =Details("Naveen",23)
d1.compare(d2)
print(d1.name)
print(d2.name)


