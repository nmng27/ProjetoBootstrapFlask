class Funcionario:
    def __init__(self,nome,email,cargo):
        self.__nome = nome
        self.__email = email 
        self.__cargo = cargo
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_cargo(self):
        return self.__cargo
    def set_nome(self,nome):
        self.__nome = nome
    def set_email(self,email):
        self.__email = email
    def set_cargo(self,cargo):
        self.__cargo = cargo
        