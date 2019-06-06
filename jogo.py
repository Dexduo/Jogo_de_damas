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

qtd_cima = 15
qtd_baixo = 15

while qtd_cima != 0 or qtd_baixo !=0:

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

	if qtd_cima == 0:
		print("O vencedor é o usuário de Baixo")
	if qtd_baixo == 0:
		print("O vencedor é o usuário de Cima")




	nova_pos(tab, peca, jogador_vez, lin1, col1, lin2, col2, qtd_cima, qtd_baixo)
	tabuleiro(tab)






tabuleiro(tab)