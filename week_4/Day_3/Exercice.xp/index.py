# Exercice 1

keys = ['Ten', 'Twenty', 'Thirty'];
values = [10, 20, 30];
result=dict(zip(keys,values));
print(result);

# Exercice 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8};
prix=0;
for key,value in family.items():
    if value<3:
        print(key+" must pay:0$\n");
        prix +=0;
    elif value>3 and value<12:
        print (key + "must pay:10$\n");
        prix+=10;
    elif value>12:
        print(key + "must pay:15$\n");
        prix+=15;
    else:
        break;

print ("the totale cost for the movies is {}$".format(prix));


familly={};
while True:
    nouveau=input("Type 'quit' to exit the entering family's member or Enter to add menber");
    if nouveau=='quit':
        break;
    else:
        nom_=input("Enter the name of the family's menber");
        age_=input("Enter the age");
        familly[nom_]=age_;

print(familly.items)


# Exercice 3

brand = {
    "name": "Zara" 
"creation_date": 1975 
"creator_name": "Amancio" "Ortega Gaona 
"type_of_clothes": ["men", "women", "children", "home"] 
"international_competitors": ["Gap", "H&M", "Benetton"]
"number_stores": 7000 
"major_color":{  
    "France": "blue", 
    "Spain": "red", 
    "US": ["pink", "green"]
    }
}

brand["number_stores"]=2;
print("Zara's products are destinied to anyone men, women, children");
brand["country_creation"]="spain";
if"international_competitors " in brand:
    brand["international_competitors"].append("Desigual");
print( brand ["international_competitors"]);
print( brand ["number_stores"]);
print( brand ["creation_date"]);
print( brand ["internationl_competitors"][len(brand["international_competitors"])-1] );
print( brand ["major_color"]["US"]);
print(len(brand));
for key in brand:
    print(key);

more_on_zara={
    "creation_date": 1975, 
    "number_stores": 10 000
}

brand.update(more_on_zara);
print(brand["number_stores"]);

# Exercice 4

users = ["Mickey","Minnie","Donald","Ariel","Pluto"];

#1
dic={};
for i in range (len (users)):
    dic[users[i]]=i;
print(dic);

#2
dic={};
for i in range (len(users)):
    dic[i]=users[i];
print(dic);

#3
dic={};
users.sort()
for i in range (len(users)):
    dic[users[i]]=i;
print(dic);


#4
dic={};
for i in range(len(users)):
    if "i" in users[i]:
        dic[users[i]]=i;
print(dic)
dic={};

#5
for i in range(len(users)):
    if (users[i])[0:1].casefold()=="m" or (users[i])[0:1].casefold()=="p":
        DIC[i]=users[i];
print(DIC)
