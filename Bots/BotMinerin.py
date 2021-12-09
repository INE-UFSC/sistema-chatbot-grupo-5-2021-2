from Bots.Bot import Bot
from Bots.Comando import Comando

class BotMinerin(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = [
            Comando('Você queria ter praia?', 'Sô, não é Minas que não tem mar, é o mar que não têm Minas!'),
            Comando('Pão de Queijo ou Queijo Canastra?', 'Pão de Queijo com Queijo Canastra'),
            Comando('O que significa a sigla GO?', 'GOnorante! Mas nós aqui de Minas somo Mai Gonorante ainda!'),
            Comando('Onde você mora?', 'Eu moro logo ali, na rua de cima do açouque do Valtin, debaixo da rua da Vânia mãe do Zé'),
            Comando('Qual o verdadeiro truco?', 'O truco de verdade é o trucão com manilha fixa! Esses paulistas que inventam esse trem de manilha alta'),
            Comando('Você é atleticano ou cruzeirense?', 'GALOOOOOO!')]
        self.__mensagem_de_erro = 'Atrapaiô o trem tudo!'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    @property
    def mensagem_de_erro(self):
        return self.__mensagem_de_erro

    @mensagem_de_erro.setter
    def mensagem_de_erro(self, mensagem_de_erro):
        self.__mensagem_de_erro = mensagem_de_erro

    def apresentacao(self):
        return f'Aoba, bão ô não?! Prazer, sou o {self.__nome}. E ocê, cê é fí de quem?'

    def boas_vindas(self):
        return f'Prazer, {self.nome}! Eu tenho um primo em Uberlândia com esse mesmo nome.'

    def despedida(self):
        return f'Vai não sô, tá cedo!! Fica só mais um cadin, vou passar um cafezin nesse instante.'
