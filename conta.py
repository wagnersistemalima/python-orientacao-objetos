class Conta:

    def __init__(self, numero: int, titular: str, saldo: float, limite: float):
        print("Construindo uma conta!")
        self.__numero = numero
        self.__titular = titular.lower().capitalize()
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    # getters

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def titular(self) -> str:
        return self.__titular

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def limite(self) -> float:
        return self.__limite

    # metodos statico

    @staticmethod
    def codigo_banco() -> str:
        return "001"

    @staticmethod
    def lista_codigos_bancos():
        return {"BB": "01", "Caixa": "104", "Bradesco": "237"}

    # setters

    @limite.setter
    def limite(self, limite: float):
        self.__limite = limite

    # metodos

    def extrato(self):
        print("Titular: {}\nSaldo: {}\n".format(self.__titular, self.__saldo))

    def deposita(self, valor: float):
        self.__saldo += valor
        print("Depositando......")

    def saque(self, valor: float):
        if self.__valida_retirada(valor):
            self.__saldo -= valor
            print("Sacando......")

        else:
            print("Ops ultrapassou o limite! para o valor {}".format(valor))

    def transeferir(self, valor: float, destino):
        if self.__valida_retirada(valor):
            self.saque(valor)
            destino.deposita(valor)

    # metodo privado

    def __valida_retirada(self, valor) -> bool:
        valor_disponivel_para_retirada = self.__saldo + self.limite
        return valor_disponivel_para_retirada >= valor
