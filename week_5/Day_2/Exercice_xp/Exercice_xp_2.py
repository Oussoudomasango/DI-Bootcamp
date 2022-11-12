class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        return ("vitesse de course de {}: {}".format(self.name,int(self.weight/self.age*10)))
    def fight(self,other_dog):
        if (self.run_speed()*self.weight ) > (other_dog.run_speed()*other_dog.weight):
            return f'{self.name} win'
        else:
            return f'{other_dog.name} is win'

if __name__=='__main__':
    milou = Dog("Milou",2,12)
    wawou = Dog("Wawou",3,10)
    michel = Dog("Michel",4,8)


    print(milou.bark())
    print(wawou.bark())
    print(michel.bark())

    print(milou.run_speed())
    print(wawou.run_speed())
    print(michel.run_speed())

    print(milou.fight(wawou))
    print(wawou.fight(milou))
    print(michel.fight(milou))