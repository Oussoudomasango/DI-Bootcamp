class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

Cat1=Cat('Hackamaru',9);
Cat2=Cat('Mousse',8);
Cat3=Cat('Passpass',10);


def oldest(age1,age2,age3):
    l=[age1,age2,age3];
    G_age=max(l);
    if G_age==Cat1.age:
    	print(f'The oldest cat is {Cat1.name}, and is {Cat1.age} years old')
    elif G_age==Cat2.age:
            print(f'The oldest cat is {Cat2.name}, and is {Cat2.age} years old')
    else:
        print(f'The oldest cat is {Cat3.name}, and is {Cat3.age} years old')

oldest(Cat1.age,Cat2.age,Cat3.age)

