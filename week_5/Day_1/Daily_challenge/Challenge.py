class Farm():
    def __init__(self, farm):
        self.name=farm + 'farm'
        self.animal_lis=[]
        self.values=[]
        print(self.name)
    
    def add_animal(self,name,num=1):
        if name in self.animal_lis:
            self.values[self.animal_lis.index(name)]=self.values[self.animal_lis.index(name)]+num
        else:
            self.animal_lis.append(name)
            self.values.append(num)
    
    def get_info(self):
        for e in self.animal_lis:
            print(e,' : ',self.values[self.animal_lis.index(e)])
        print('\n')
        x='\tE-I-E-I-0!'
        return x

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat',12)
print(macdonald.get_info())
        