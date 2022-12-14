# Exercise 1 – Random Sentence Generator
#1-2-3
#Dict
"""
def get_words_from_file():
     with open('mot.txt') as f:
         mot = {}
         for line in f:
             if line[0] in mot :
                 mot.update({line[0] : mot[line[0]]+' '+line[0:len(line)-1]})
             else:
                 mot.update({line[0] : line})
     return mot

#list
"""
def get_words_from_file():
    with open('mot.txt') as f:
        mot = []
        for line in f:
            mot.append(line[0:len(line)-1])
    return mot
#4
def get_random_sentence(length=6):
    import random
    sentence = ""
    mots = get_words_from_file()
    for x in range (0,length):
        sentence += mots[random.randint(0,len(mots))] + ' '
    return sentence


#5
# mot = get_random_sentence().lower()
# print(mot)

#6
"""
def main():
    print("\nCe programme génère une phrase pour vour.\n"
          "C'est à vous de spécifier la taille de la phrase.\n")
    length = int(input('Entrez la taille (2 à 20) : '))
    if length >= 2 and length <= 20:
        print(get_random_sentence(length))
    else:
        print('Error')

main()
"""

# Exercice 2 : Travailler Avec JSON
import json
sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
#1
sampleJson = json.loads(sampleJson)
print(sampleJson['company']["employee"]['payable']['salary'])
sampleJson['company']['employee'].update({'birth_date':''})
print(sampleJson)

#3
import json
jsonFile = 'fic.json'
with open(jsonFile,'w') as jF:
    json.dump(sampleJson,jF)
