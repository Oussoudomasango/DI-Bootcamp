#Challenge_1
print("\nChallenge 1\n")

number= int (input("Donner un nombre:\t"))
length= int (input("Veuiller entrer le nombre de multiple dont vous voulez:\t"))
liste =[]
for i in range(1,length+1):
    liste.append(number*i)
print(f"number: {number} - length: {length} => ",liste)

#Challenge_2
print("\nChallenge 2\n")

mot = input("Votre terme:\t")
n = len(mot)
mot=list(mot.rstrip())
if n<2:
    print(''.join(mot))
else:
    j=0
    for i in range(n):
        if(mot[j]!=mot[i]):
            j+=1
            mot[j]=mot[i]
    j+=1
    mot = mot[:j]
print(''.join(mot))