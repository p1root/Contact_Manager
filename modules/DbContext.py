import sqlite3
from modules.model import Contact
import pathlib


class Database:
    __con = sqlite3.connect(pathlib.Path(
        __file__).parent.joinpath("ContactDB.db"))
    __cur = __con.cursor()

    def __init__(self):

        self.__cur.execute(
            'CREATE TABLE IF NOT EXISTS Contact(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT ,EMAIL TEXT , PHONE TEXT)')
        
    def loadAll(self, item="*"):
        res = self.__cur.execute(f' SELECT {item} FROM Contact ')
        temp = res.fetchall()
        data = []
        for t in temp:
            data.append(Contact(t[0] , t[1], t[2], t[3]))
        return data

    def loadWithName(self, name:str):
        res = self.__cur.execute(f' SELECT * FROM Contact where NAME == "{name}"')
        temp = res.fetchall()
        data = []
        for i in temp:
            data.append(Contact(i[0] , i[1], i[2], i[3]))
        return data

    def addContact(self, Contact:Contact):
        self.__cur.executemany(f'INSERT INTO Contact (NAME , EMAIL , PHONE) VALUES (? , ?, ?)', [
            (Contact.name, Contact.phone, Contact.email)])
        self.__con.commit()

    def updateContact(self, Contact:Contact):
        self.__cur.execute(
            f'UPDATE Contact SET NAME = "{Contact.name}" ,EMAIL = "{Contact.email}" , PHONE = "{Contact.phone}" WHERE ID={Contact.id}')
        self.__con.commit()

    def remove(self, ID):
        self.__cur.execute(f'DELETE FROM Contact WHERE ID = {ID}')
        self.__con.commit()
