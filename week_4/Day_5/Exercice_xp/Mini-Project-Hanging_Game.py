# The Hanging Game
print("The Hanging Game\n")

import random

wordslist = ['correction','childish','beach','python','assertive','interference','complete','share','credit card','rush','south']
word=random.choice(wordslist)
def playTheGame():

    print("list of words")
    print(wordslist)
    yword=input('choose a word : ')
    while (yword not in wordslist):
        yword=input('word must be in the list so choose a word :')
    hiddenWord="*"*len(word)
    print("*"*len(word))
    hidden=word.split("");
playTheGame()




