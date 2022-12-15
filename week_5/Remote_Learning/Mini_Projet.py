class Human:

    def __init__(self,name,age,priority,blood_type):
        self.id_number = "Unknown"
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        # Partie 2 [
        self.family = []
        # Partie 2 ]

    # Partie 2 [
    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)

    # Partie 2 ]

class Queue:
    humans = []

    def add_person(self, person):
        if person.age > 60 or person.priority == True :
            self.humans.insert(0,person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        return self.humans.index(person)

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        self.humans.pop(index1)
        self.humans.insert(person2)
        self.humans.pop(index2)
        self.humans.insert(person1)

    def get_next(self):
        try:
            supp = self.humans[0]
            self.humans.pop(0)
        except:
            supp = None
        return supp

    def get_next_blood_type(self, blood_type):
        supp = None
        for person in self.humans:
            if person.blood_type == blood_type:
                supp = person
                self.humans.pop(self.humans.index(person))
                return supp
        return supp

    def sort_by_age(self):
        humain = self.humans.copy()
        self.humans = []
        for person in humain:
            if person.priority == True:
                self.humans.append(person)
        for person in humain:
            if person.age > 60 and person not in self.humans:
                self.humans.append(person)
        for person in humain:
            if person.age <= 60 and person not in self.humans:
                self.humans.append(person)
        for person in self.humans:
            person.id_number = self.humans.index(person) + 1

person = Human("John",12,True,"AB")
person1 = Human("Asah",63,True,"A")
person2 = Human("Sarah",61,False,"A")
File = Queue()
File.add_person(person)
File.add_person(person1)
File.add_person(person2)
File.sort_by_age()
#print(File.get_next_blood_type("A").name)

print(File.get_next().name)
print(File.get_next().name)
print(File.get_next().name)


# Partie 2
print()
person1.add_family_member(person)
print(person.family[0].name)
print(person1.family[0].name)
