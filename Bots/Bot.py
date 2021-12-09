from abc import ABC, abstractmethod
from Comando import Comando

class Bot(ABC):

    def __init__(self, nome, comandos=[]):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def adiciona_comando(self, comando, resposta):
        novo_comando = Comando(comando, resposta)

    def remove_comando(self, comando):
        if comando in self.comandos:
            self.comandos.remove(comando)

    def mostra_comandos(self):
        for i, comando in enumerate(self.comandos):
            print(f'{i} - {comando.pergunta}')

    def executa_comando(self, comando):
        if comando.isnumeric() and (comando < len(self.comandos)):
            print(f'--> {self.nome} diz: Você disse "{self.comandos[comando]}"')
            print(f' --> Eu te respondo: "{self.comandos[comando].resposta}"')
        else:
            print(f'Digite um comando válido.')

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass
