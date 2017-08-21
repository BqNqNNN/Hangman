class player:
    __name=""
    __passwd=""
    __score=[]
    __idP=-1

    def __init__(self,name,passwd,score,idP):
        self.__name=name
        self.__passwd=passwd
        self.__score.append(score)
        self.__idP=idP



    def set_name(self,name):
        self.__name=name

    def set_passwd(self,passwd):
        self.__passwd=passwd

    def set_score(self,score):
        self.__score.append(score)


    def get_idP(self):
        return self.__idP
    def get_name(self):
        return self.__name
    def get_passwd(self):
        return self.__passwd
    def get_score(self):
        return self.__score