from player import *
from game import *
import getpass
import datetime



_tPlayers=[]
_pDbName="player"
_dbWord="words"
scoreP=-1



def score():
    conn = sqlite3.connect(_pDbName + ".db")
    cursor = conn.cursor()
    query = " select name,score,date from players inner join scores where id=ids and ids="+str(_tPlayers[0].get_idP())+" order by score DESC;"
    Rslt = cursor.execute(query)
    print("Player : ",_tPlayers[0].get_name())
    print("\n")
    print("         Score",end="")
    print("                         Date")
    for row in Rslt:
        print("         ",row[1],end="")
        print("                         ",row[2])


def scoreAll():
    conn = sqlite3.connect(_pDbName + ".db")
    cursor = conn.cursor()
    query = " select name,score from players inner join scores where id=ids order by score DESC;"
    Rslt = cursor.execute(query)
    print("Player           score")
    for row in Rslt:
        print(row[0], end="")
        print("              ", row[1])


def menu():
    
    print("\n\n\t\t\t******* Welcom to the HangMan *******\n\n\n")
    _mchoice = int(input("..1 New game.\n..2 check your previous scores.\n..3 Highest Score on the game.\n..4 Exit.\n  -> "))
    if(_mchoice==1):

        scoreP=game(_dbWord)

        ## save score to dataBase

        conn = sqlite3.connect(_pDbName + ".db")
        conn.cursor()
        query = " insert into scores (ids,score,date) values ('"+str(_tPlayers[0].get_idP())+"','"+str(scoreP)+"','"+str(datetime.datetime.now())+"');"
        conn.execute(query)
        conn.commit()
        menu()

    if(_mchoice==2):

        score()
        menu()

    if(_mchoice==3):
        scoreAll()
        menu()
    if(_mchoice==4):
        exit()


def loadPlayersFromDB(_pDbName):
    conn1 = sqlite3.connect(_pDbName + ".db")

    cur1=conn1.cursor()
    query="select * from players;"

    result = cur1.execute(query)

    for row in result:
        _tPlayers.append(player(row[1],row[2],))




def playersTable(_pDbName):
    if (_pDbName!= None):
        conn = sqlite3.connect(_pDbName+".db")
        query = "CREATE TABLE players(" \
                " id INTEGER PRIMARY KEY AUTOINCREMENT," \
                "name text," \
                "passwd text," \
                "UNIQUE(name, passwd)" \
                ");"
        conn.execute(query)
        query = "CREATE TABLE scores(" \
                "ids INTEGER," \
                "score integer," \
                "date text"\
                ");"
        conn.execute(query)
    else:
        print("please provide a database name !")

def register(_pDbName):
        name = input("Pseudo :")
        if(len(name)>4):
            passwd = getpass.getpass("Password :")
            if (len(passwd)>4):
                now = datetime.datetime.now()

                conn1 = sqlite3.connect(_pDbName+".db")
                cursor1=conn1.cursor()
                #name, passwd, score = line.split(";", 2)


                try:
                    query = "INSERT INTO players (name,passwd) VALUES ('" + str(name) + "','" + str(passwd) + "');"
                    cursor1.execute(query)
                    idP = cursor1.lastrowid
                    conn1.commit()
                    _tPlayers.append(player(name, passwd,0,idP))

                    query= " insert into scores (ids,score,date) values ('"+str(idP)+"','0','"+str(now)+"');"
                    conn1.execute(query)
                    conn1.commit()
                except sqlite3.IntegrityError as err:
                    conn1.close()
                    print("Player already exist please sign-in")
                    newGame()

                    #!Player already exist in Database

            else:
                print("Pass must be > 4")
        else:
            print("user must be > 4 ")


def exist(_pDbName):
    name = input("Pseudo :")
    if (len(name) > 4):
        passwd = getpass.getpass("Password :")
        if (len(passwd) > 4):
            conn1 = sqlite3.connect(_pDbName + ".db")
            cursor1 = conn1.cursor()

            query = "select id from players where name='" + str(name) + "' and passwd ='" + str(passwd) + "';"
            results = cursor1.execute(query)
            data=cursor1.fetchone()

            if(data):
                results = cursor1.execute(query)
                for row in results:
                    idP = row[0]

    ##Connect to the second Score table


                query = " select * from scores where ids='"+str(idP)+"';"
                results = cursor1.execute(query)

                lScores ={0}
                for row in results:
                    lScores.add(row[1])
                    print("The player {} has id {} and scored {} on {}".format(name, row[0], row[1], row[2] ) )
                _tPlayers.append(player(name,passwd,lScores,idP))
            else:
              print("Error")
              newGame()
        else:
            print("Pass must be > 4")
            newGame()
    else:
        print("user must be > 4 ")
        newGame()




def newGame():


    print("\n\n\t\t\t******* Welcom to the HangMan *******\n\n\n")
    _NO=int(input("..1  Register.\n..2  Sign-in.\n..3 create DataBase. \n -> "))
    if (_NO==1 ):
       register(_pDbName)

    elif(_NO==2) :
        exist(_pDbName)
    else:
        playersTable(_pDbName)

    
    menu()
