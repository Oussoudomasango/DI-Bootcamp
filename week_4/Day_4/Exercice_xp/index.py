# Exercice 1
print("\n Exercice 1 \n");
def display_message():
    print("Helle evryone i'm learning function with python.");

display_message();

# Exercice 2
print("\n Exercice 2 \n");

def favorit_book(title):
    print("One of my favorite book is",title);

favorit_book(" 'Reflechissez et devenez riche de napoleon hill' ");

# Exercice 3
print("\n Exercice 3 \n");

def describe_city(city,country="Burkina Faso"):
    print (city," is in ", country);

describe_city("Ouagadougou");

# Exercice 4
print("\n Exercice 4 \n");

import random;

def verfi():
    number_U=input("Enter a number between 1 and 100: ");
    number_C=random.randrange(1,100);
    
    if number_C==number_U:
        print("Good is your number")
    else:
        print("Sorry, try again!! the number of computer is :" number_C);


verfi();

# Exercice 5
print("\n Exercice 5 \n");

def make_shirt(size="large",message="I love python"):
    print(f"The size of the shirt is {size} and the text is {message}")
make_shirt();
make_shirt(size="medium");
make_shirt("any",message="I learn java-script");

# Exercice 6
print("\n Exercice 6 \n");

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel'];

def show_magicians(names):
    for i in names:
        print(i);


def make_great(names):
    for i,name in enumerate(names):
        names[i] = name + "the Great";

make_great(magician_names);

show_magicians(magician_names);

# Exercice 7
print("\n Exercice 7 \n");

def get_random_temp():
    return random.randrange(-10,40);

result= [get_random_temp() for i in range(10)]
print(result)

def main():
    temp = get_random_temp();
    print(f"The temperature right now is {temp} degrees Celsius.");
    if(temp < 0 ):
        print(" Brrr, that’s freezing! Wear some extra layers today");
    elif(temp>0 or temp<=16):
        print("Quite chilly! Don’t forget your coat");
    elif(temp>16 or temp<=23):
        print("Relatively nice");
    elif(temp>23 or temp<=32):
        print("Litle bit hot");
    else:
        print("Very hot");

main ();
def get_random_temp(season):
    if season == "Winter":
        return random.randrange(-10,16);
    elif season == "Automn" or season == "Fall":
        return random.randrange(16,23);
    elif season == "Summer":
         return random.randrange(24,32);
    elif season == "Spring":
         return random.randrange(33,40);
    else:
        return random.randrange(-10,40);

def  main():
    season = input("Enter for a season : ");
    temp = get_random_temp(season);
      print(f"The temperature right now is {temp} degrees Celsius.");
    if(temp < 0 ):
        print(" Brrr, that’s freezing! Wear some extra layers today");
    elif(temp>0 or temp<=16):
        print("Quite chilly! Don’t forget your coat");
    elif(temp>16 or temp<=23):
        print("Relatively nice");
    elif(temp>23 or temp<=32):
        print("Litle bit hot");
    else:
        print("Very hot");


main()
    

