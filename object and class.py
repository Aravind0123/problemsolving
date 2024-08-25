class Cricket:
    def __init__(self,name,id):
        self.name= name
        self.id = id
    def player(self):
        print(self.name,"with",self.id)
p =Cricket("Aravind",101)
p.player()