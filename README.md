# python-orientacao-objetos

## Diagrama

![alter txt](https://github.com/wagnersistemalima/python-orientacao-objetos/blob/main/image/diagrama.png)

* A Conta() está dentro de um módulo — que em algumas linguagens receberá o nome de package ou namespace
* conta.py pode conter varias classes

## Classe

* Uma classe deve ter apenas uma responsabilidade (ou deve ter apenas uma razão para existir)
em outras palavras, ela não deve assumir responsabilidades que não são delas.

```
class Conta:

```

## Construtores

* __init__ é uma função implicita

* Sendo uma função automática, receberá um nome especial. Adicionaremos dois caracteres _ antes e depois do nome da função construtora,
para criarmos __init__. O Python constrói o objeto, cria um lugar na memória e depois chama a função __init__. Como demonstração, segue o código:

```
    def __init__(self, numero: int, titular: str, saldo: float, limite: float):
        print("Construindo uma conta!")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
```
## metodos para acessar objetos

* atributos privados e modificadores de acesso python self.__atributo

```
    def __init__(self, numero: int, titular: str, saldo: float, limite: float):
        print("Construindo uma conta!")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
```
* Os atributos irão receber o nome da classe como prefixo. Ex: _Conta__titular

## Encapsulamento

```
    def get_numero(self) -> int:
        return self.__numero
    
    def get_titular(self) -> str:
        return self.__titular
    
    def get_saldo(self) -> float:
        return self.__saldo
    
    def get_limite(self) -> float:
        return self.__limite

```

## Na linguagem Python, os métodos que dão acesso são nomeados como properties.

* Com isto, indicamos que este método representa uma propriedade

```
    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
```
## Criando metodos na classe privado

* Utilazar __nome_do_metodo():

```
    def __valida_retirada(self, valor) -> bool:
        valor_disponivel_para_retirada = self.__saldo + self.limite
        return valor_disponivel_para_retirada >= valor
```

## Metodos estaticos da classe

* Adicionando um metodo statico da classe para criar um codigo do banco
* Anotação @staticmethod
* Nao precisa da referencia self

```
    @staticmethod
    def codigo_banco() -> str:
        return "001"

```
