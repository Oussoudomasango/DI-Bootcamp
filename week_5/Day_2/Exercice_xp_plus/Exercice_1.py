#Exercise 1 : Family
'''

'''
class Family:
    def __init__(self,last_name):
        self.members=[
                        {'name':'Michael','age':35,'gender':'Male','is_child':False},
                        {'name':'Sarah','age':37,'gender':'Female','is_child':False}
                    ]
        self.last_name=last_name
    def born(self,**kwargs):
        new={}
        for k,v in kwargs.items():
            new[k] = v
        self.members.append(new)
        print("congratulating the family")
        
    def is_18(self,nameMembers):
        for member in self.members:
            if nameMembers==member['name'] and member['age'] > 18:
                print(member['name']," a plus de 18 ans")
                return True
        print(member['name']," a moin de 18 ans")
        return False
    def family_presentation(self):
        print("the last-name: ",self.last_name)
        for member in self.members:
            #print the name of the family
            print(member['name'])
            
if __name__=='__main__':
    family1 = Family('SANGO')
    family1.born(name="Donald",age=27,gender="Male",is_child=True)
    print(family1.is_18("Sarah"))
    family1.family_presentation()
