import random

mot=input ("Veuillez entrer un mots");
while len(mot)!=10:
    if(len(mot)<10):
         print("string not long enough");
    elif (len(mot)>10):
        print("string too long");
    mot=input("Veuillez entrer un nouveau mot de  ou pharse de 10 lettres");


print ("le premier charactère est : {} et le dernier est : {}".format(mot[0],mot[9]));

mots = input ("Veuillez entrer une nouvelle valeur");

for x in range (len(mots)):
    print (mots[0:x+1])

mots1 = input ("Veuillez entrer un autre mots");
m = ''.join(random.sample(mots1,len(mots1)))