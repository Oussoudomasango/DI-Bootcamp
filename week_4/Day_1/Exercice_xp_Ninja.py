# Exercice 1
#explication

# Exercice 2
# $ py n'est pas reconnu par windows sur ma machine 
# donc

# Exercice 3

#3 <= 3 < 9
# True

#3 == 3 == 3
#True

# bool(0)
#False

# bool(5 == "5")
# False

# bool(4 == 4) == bool("4" == "4")
# True

# bool(bool(None))
# False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

#print("x is", x)
#x is True

#print("y is", y)
#y is False

#print("a:", a)
# a: 5

#print("b:", b)
#b: 10


# Exercice 4

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,sunt in culpa qui officia deserunt mollit anim id est laborum."
 
print(len(my_text));

# Exercice 5

mot1=input("Veuillez entre un long text sans 'A': ");
if ('A' in mot1):
    print("Veuillez entrer un text sans 'A' \n");
    mot1=input("\nVeuillez Entrer à nouveau : " );
else:
    mot2=input("\nveuillez entrer un deuxième text : ");
    if('A' in mot2):
        print("Veuillez entrer un text sans 'A' \n");
        mot2=input("\nVeuillez Entrer à nouveau : " );
    elif(len(mot1)>len(mot2)):
        print("Le premier est le plus long");
    elif(len(mot1)<len(mot2)):
        print ("Felicitation le deuxième mots est plus long")
    else:
        print("veuillez reprendre le jeux");



