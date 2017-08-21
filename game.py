from random import *
import sqlite3


_dbWord="words" #DataBase name

def random_line(afile): #generate random line from the given file
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line


def geneWord(_dbWord):  # Generate a random word from the dataBase

    '''
    with open(_dbWord+".txt","r") as file:

        line=random_line(file)
        wordArray=[]

        typew, hint, word = line.split(";")
        wordArray.append(typew)
        wordArray.append(hint)
        wordArray.append(word)





    conn = sqlite3.connect(_dbWord + ".db")
    cursor = conn.cursor()

    query = " select * from words order by Random() limit 1;"
    Rslt = cursor.execute(query)

    wordArray = []

    for row in Rslt:
        wordArray.append(row[0])
        wordArray.append(row[1])
        wordArray.append(row[2])
    '''
    lastWord = ["SYNONYME", "combat", "bataille",
                "DEFINITION", "Un ensemble de regles etablies", "protocole",
                "ANTONYME", "universel", "national",
                "SYNONYME", "danseuse", "ballerine",
                "DEFINITION", "coller a laide du ruban adhesif de marque Scotch", "scotcher",
                "SYNONYME", "admirable", "ravissant",
                "SYNONYME", "penalite", "sanction",
                "ANTONYME", "couteux", "gratuit",
                "ANTONYME", "horrible", "admirable",
                "DEFINITION", "personne dependante dune drogue, dune activite", "addict",
                "DEFINITION", "celui qui enleve une personne pour obtenir une rancon", "kidnappeur",
                "SYNONYME", "effrayant", "terrifiant",
                "ANTONYME", "terrifiant", "rassurant"
    ]
    rnd=1
    while rnd %3 != 0:
        rnd=randrange(13)

    wordArray = []

    type=lastWord[rnd]
    hint=lastWord[rnd+1]
    word=lastWord[rnd+2]


    wordArray.append(type)
    wordArray.append(hint)
    wordArray.append(word)

    print(wordArray)

    return wordArray


def cls():
    print ("\n" * 30)

def game(_dbWord):
    _word = geneWord(_dbWord)

    print("The type of word is : {}".format(_word[0]))
    print("The Hint of word is : {} \n".format(_word[1]))

    nbguessing = 0
    correct = 0

    length = len(_word[2])
    code = "*" * length
    score=1
    guessW = list(code)

    while (correct != length and nbguessing < 6):
        lettre = input("Guess a letter : ")
        tr = False
        for index, lword in enumerate(_word[2]):
            if (lword == lettre):
                # correct
                guessW[index] = lword
                correct += 1
                tr = True
                score+=correct*2

        print("".join(guessW))
        print('\n')
        if (tr == False):
            print("\nIncorrect you still have {} chances.".format(5-nbguessing))
            nbguessing += 1
            score-=1
            hangman_graphic(nbguessing)
            if(nbguessing==6):
                print("Game Over")
    return score










def hangman_graphic(guesses):
    if guesses == 0:
        print("                                         ________      ")
        print("                                         |      |      ")
        print("                                         |             ")
        print("                                         |             ")
        print("                                         |             ")
        print("                                         |             ")
    elif guesses == 1:
        print("                                         ________      ")
        print("                                         |      |      ")
        print("                                         |      0      ")
        print("                                         |             ")
        print("                                         |             ")
        print("                                         |             ")
    elif guesses == 2:
        print("                                         ________      ")
        print("                                         |      |      ")
        print("                                         |      0      ")
        print("                                         |     /       ")
        print("                                         |             ")
        print("                                         |             ")
    elif guesses == 3:
        print("                                         ________      ")
        print("                                         |      |      ")
        print("                                         |      0      ")
        print("                                         |     /|      ")
        print("                                         |             ")
        print("                                         |             ")
    elif guesses == 4:
        print("                                         ________      ")
        print("                                         |      |      ")
        print("                                         |      0      ")
        print("                                         |     /|\     ")
        print("                                         |             ")
        print("                                         |             ")
    elif guesses == 5:
        print("                                         ________      ")
        print("                                         |      |      ")
        print("                                         |      0      ")
        print("                                         |     /|\     ")
        print("                                         |     /       ")
        print("                                         |             ")
    else:
        print("                                         ________      ")
        print("                                         |      |      ")
        print("                                         |      0      ")
        print("                                         |     /|\     ")
        print("                                         |     / \     ")
        print("                                         |             ")

