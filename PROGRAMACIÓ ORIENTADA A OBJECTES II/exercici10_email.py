# exercici10_email.py
# Autor: Joel Garcia
# Descripció: Classe CompteUsuari amb email privat i validació bàsica al setter.

class CompteUsuari:
    def __init__(self):
        self.__email = ""

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nou_email):
        if "@" in nou_email and "." in nou_email:
            self.__email = nou_email
