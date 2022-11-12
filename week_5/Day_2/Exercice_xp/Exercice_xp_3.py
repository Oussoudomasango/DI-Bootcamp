import random
#Exercise 3 : Dogs Domesticat
from Exercice_xp_2 import Dog
class PetDog(Dog):
    def __init__(self,name,age,weight):
        super().__init__(name,age,weight)
        self.trained= False
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self,*dog_names):
        print("{} and {} all play together ".format((",".join(dog_names)),self.name))
        
    def do_a_trick(self):
        self.liste = [" does a barrel roll"," stands on his back legs"," shakes your hand"," plays dead"]
        if self.trained:
            print(self.name,random.choice(self.liste))

if __name__=='__main__':
    bruno = PetDog("bruno",1,5)
    bruno.train()
    bruno.play("michel","milou","champion")
    bruno.do_a_trick()
        