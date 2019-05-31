from tab import tabuleiro
from tab import nova_pos
from a_definir import comer
tab = [
	["#", "o", "#", "o", "#", "o", "#", "o", "#", "o"],
	["o", "#", "o", "#", "o", "#", "o", "#", "o", "#"],
	["#", "o", "#", "o", "#", "o", "#", "o", "#", "o"],
	[" ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
	["#", " ", "#", " ", "#", " ", "#", " ", "#", " "],
	[" ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
	["#", " ", "#", " ", "#", " ", "#", " ", "#", " "],
	["@", "#", "@", "#", "@", "#", "@", "#", "@", "#"],
	["#", "@", "#", "@", "#", "@", "#", "@", "#", "@"],
	["@", "#", "@", "#", "@", "#", "@", "#", "@", "#"]
]

tabuleiro(tab)

comida_cima = 0
comida_baixa = 0

while comida_baixa<=15 or comida_cima<=15:

	jogador_vez = input("Quem vai jogar agora? ")
	jogada = input("Faça sua jogada: ")

	nova_pos(tab, jogada)
	tabuleiro(tab)
	comer(tab, jogada)



tabuleiro(tab)