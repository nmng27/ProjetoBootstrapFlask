class Usuario:
    def __init__(self,email,senha):
        self.__email = email
        self.__senha = senha 
    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email = email
    def get_senha(self):
        return self.__senha
    def set_senha(self,senha):
        self.__senha = senha

    