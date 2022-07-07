class Cliente:

    def __init__(self, nome: str):
        print("Criando cliente...")
        self.__nome = nome.lower().title()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
