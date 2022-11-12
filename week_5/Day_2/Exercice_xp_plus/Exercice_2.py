from Exercice_1  import Family
#Exercise 2 : TheIncredibles Family
class TheIncredibles(Family):
    def __init__(self,last_name):
        super().__init__(last_name)
        self.members = [
                        {'name':'Michael','age':12,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
                        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
                    ]
    def use_power(self):
        try:
            for member in members:
                if member['age']>35:
                    print(member['name']," have ",member['power']," like power")
        except:
            print("you are not over 18 years old")
            
    def incredible_presentation(self):
        super(TheIncredibles,self).family_presentation()
        #imprime le nom et le pouvoir incroyables de tous les membres
        for member in self.members:
            print(member['name'],' have ',member['power'],' like power')


if __name__=='__main__':
    family2 = TheIncredibles("SANOU")
    family2.incredible_presentation()
    family2.born(name="Baby Jack",age=1,gender="Male",is_child=True,power="Unknown Power",incredible_name="UnknownJack")
    #Call the incredible_presentation method again.
    family2.incredible_presentation()