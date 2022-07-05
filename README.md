# python-orientacao-objetos

## Diagrama

![alter txt](https://github.com/wagnersistemalima/python-orientacao-objetos/blob/main/image/diagrama.png)

* A Conta() está dentro de um módulo — que em algumas linguagens receberá o nome de package ou namespace
* conta.py pode conter varias classes

## Classe

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
