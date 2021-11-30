#encoding: utf-8
from Bots.BotManezinho import BotManezinho
from Bots.BotMinerin import BotMinerin
from SistemaChatBot import SistemaChatBot as scb

###construa a lista de bots disponíveis aqui
lista_bots = [BotMinerin("João"), BotManezinho('Ixtepô')]

sys = scb.SistemaChatBot("GoBotsRegionais", lista_bots)
sys.inicio()