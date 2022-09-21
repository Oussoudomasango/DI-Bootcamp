# Exercice 1
print("Hello world \n"*4);

# Exercice 2
total=(99*99*99)*8;
print(total);

# Exercice 3
#>>> 5 < 3
#False
#>>> 3 == 3
#True
#>>> 3 == "3"
#False
#>>> "3" > 3

#>>> "Hello" == "hello"
#False

#Exercice 4
computer_brand = "Lenovo";
print ("I have a {} computer".format(computer_brand));

#Exercice 5
name="Ahldaïr";
age=27;
shoe_size=43;
info="Hello everyone my name is: {} i'm {} years old and my shoe_size is: {}".format(name,age,shoe_size);
print(info);

#Exercice 6
a=5;
b=6;
if a>b:
    print("Hello World");

#Exercice 7
number=input("Veuillez entrer un nombre pour que nous vérifion s'il est paire ou impaire");
if(number%2)==0:
    print("{} est paire ".format(number))
else:
    print("{} n'est pas paire")

#Exercice 8
nom="Ahldaïr";
nom2=input("Quel est votre nom : ");
if(nom==nom2):
    print("AH bon vous voulez me dire que nous avons le même nom !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
else:
    print("Bienvenu {} , mon nom est {} ".format(nom2,nom));

#Exercice 9
taille=input("Veuillez entrer votre taille: ");
if(taille>145):
    print("You are tall enought to ride");
else:
    print ("You need to grow some more to ride");
