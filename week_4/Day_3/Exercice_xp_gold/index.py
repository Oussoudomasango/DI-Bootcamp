#Exercice 1
print("\nExercice 1\n")

birthday={'naruto':'1960/12/24',
           'sasuke':'2009/02/05',
           'orochimaru':'1994/03/29',
           'minato':'2003/07/16',
           'pain':'2001/06/2001'}
print(birthday);
t=0;
_name=input("Enter un name:")
for cle in birthday.keys():
    if _name==cle:
        t=1;
        print("The birthday of ",cle)
        print(birthday[_name])
if t==0:
    print("This name is not in our database");


#Exercice 2
print("\nExercice 2\n")

birthday_={'naruto':'1960/12/24',
           'sasuke':'2009/02/05',
           'orochimaru':'1994/03/29',
           'minato':'2003/07/16',
           'pain':'2001/06/2001'}
print(" Voici la base de donné ",birthday_);
t=0;
name_=input("Entrer un nom:")
for cle in brithday_.keys():
    if name==cle:
        t=1;
        print("The birthday of ", cle);
        print(birthdays[name]);
if t==0:
print("Sorry, we don't have the birthday information for ", name);
 
# Exercice 3
print("\nExercice 3\n")

_birthday={'naruto':'1960/12/24',
           'sasuke':'2009/02/05',
           'orochimaru':'1994/03/29',
           'minato':'2003/07/16',
           'pain':'2001/06/2001'}
nom=input("Veuillez entrer un nom: ");
dat=input("Veuillez entrer la date de naissance: année/mois/jour")

t=0;
for cle in _birthday.keys():
    if nom==cle:
        print(f"{nom} est dans la liste :",_birthday[nom]);
        t=1;
        break;
if t==0:
    print(f"nous ajoutons {nom} à la liste avec {dat} comme date de naissance ");
    _birthdays[nom]=dat;
    print(_birthday)

# Exercice 4
print("\nExercice 4\n")

item = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for cle,valeur in item.items():
    print (cle," prix--> ",valeur);
som=0;
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
    }

for cle,valeur in item.items():
    som+=items[cle]['price']*items[cle]['stock']
print("Prix total: ",som);