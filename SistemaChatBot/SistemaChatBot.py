from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nomeEmpresa: str, lista_bots: []):
        self.__empresa = nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        for bot in lista_bots:
            if not isinstance(bot, Bot):
                erro = f'{type(bot)}, não é Bot'
                raise TypeError(erro)
        self.__lista_bots = lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        ##mostra mensagem de boas vindas do sistema
        print(f'Olá esse é o sistema de chatbots da empresa {self.__empresa}')

    def mostra_menu(self):
        print('Os bots disponiveis no momento são:')
        for number, bot in enumerate(self.__lista_bots):
            print(f'{number} - Bot: {bot.nome} - Mensagem de apresentação {bot.apresentacao()}')
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        escolha = int(input('Digite o número do chat bot desejado: '))
        self.__bot = self.__lista_bots[escolha]
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        self.__bot.mostra_comandos()
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        escolha = str(input('Digite o comando desejado (ou -1 fechar o programa e sair): '))
        if escolha == '-1':
            return "-1"
        else:
            self.__bot.executa_comando(escolha)
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        self.boas_vindas()
        ##mostra o menu ao usuário
        self.mostra_menu()
        ##escolha do bot
        self.escolhe_bot()
        ##mostra mensagens de boas-vindas do bot escolhido
        self.__bot.boas_vindas()
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        while True:
            self.mostra_comandos_bot()
            escolha = self.le_envia_comando()
            if escolha == "-1":
                break
        ##ao sair mostrar a mensagem de despedida do bot
        self.__bot.despedida()
