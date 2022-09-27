# Exercice
from audioop import reverse
from lib2to3.pytree import convert

companie="Volkswagen, Toyota, Ford Motor, Honda, Chevrolet";
liste=companie.split(',');
print(liste);
print("There are {} manufactures/companies in the liste ".format(len(liste)));
print(" the reverse liste");
rev=list(reversed(liste))
print (sorted(rev));
j=0
n=0
for i in range(5):
    if'o' in liste[i]:
        j+=1;
print(j," manufacture's names have the letter 'o");
for i in range(5):
    if 'o' in liste[i]:
        n+=1;
print(n,"manufacture's names do not have the letter i");
liste=["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
conver=set(liste);
newList=list(conver);
taille=len(conver);
print(" set list: ",conver);
print("il y a ", taille," element dans la liste: ",newlist);