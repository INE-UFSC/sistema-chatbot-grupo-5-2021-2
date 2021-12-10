#encoding: utf-8
from Bots.BotManezinho import BotManezinho
from Bots.BotMinerin import BotMinerin
from Bots.BotEspelhado import BotEspelhado
from SistemaChatBot import SistemaChatBot as scb

###construa a lista de bots disponíveis aqui
lista_bots = [BotMinerin("João"), BotManezinho('Ixtepô'), BotEspelhado('ohnidahlepsE')]

sys = scb.SistemaChatBot("GoBots", lista_bots)
sys.inicio()