from tab import tabuleiro
from posicao import nova_pos

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

coluna = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
linha = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

# comida_cima = 0
# comida_baixa = 0

#while comida_baixa<=15 or comida_cima<=15:

jogador_vez = input("Quem vai jogar agora? ")
jogada = input("Faça sua jogada: ")

col1 = coluna[jogada[0]]
lin1 = linha[jogada[1]]
col2 = coluna[jogada[4]]
lin2 = linha[jogada[5]]

if (tab[lin1][col1] == "@" or tab[lin1][col1] == "o"):
	peca = "normal"
else:
	if tab[lin1][col1] == "&" or tab[lin1][col1] == "O":
		peca = "dama"
	else:
		peca = "invalida"

nova_pos(tab, peca, jogador_vez, lin1, col1, lin2, col2)






tabuleiro(tab)