class Iter:
    def __init__(self) -> None:
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.num<=10):
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration

values = Iter() 

for i in values:
    print(i)