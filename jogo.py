#JOSÉ EDUARDO SOARES DE LIMA NOGUEIRA - 421873
#ÍTALO FREIRE - 422025
#MANOEL JOSÉ DE ALENCAR NETO - 472831

import sys
from tab import tabuleiro
from jogada import posicao
from transformar import normal_dama

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
peca = 0

start = "S"

while start == "S" or start == "s":
	
	if len(sys.argv) == 2:
		print("Modo offline")
		print("Não fiz esse modo")

	else:
		print("Modo online")
		print()

		jogador_vez = input("Quem vai jogar agora? ")

		while qtd_cima != 0 or qtd_baixo !=0:

			#AQUI CONTAREI A QTDD DE PEÇAS ANTERIORES PARA NO FINAL DECIDIR SE O USUARIO JOGA NOVAMENTE OU NÂO
			qtd_cima_anterior = qtd_cima
			qtd_baixo_anterior = qtd_baixo

			#AQUI SÓ POR QUESTÃO DE ORGANIZAÇÃO DA LEITURA DE QUEM VAI JOGAR NA HORA
			if jogador_vez == "B":
				jogada = input("Usuário de baixo, faça sua jogada: ")
			else:
				jogada = input("Usuário de cima, faça sua jogada: ")

			col1 = coluna[jogada[0]]
			lin1 = linha[jogada[1]]
			col2 = coluna[jogada[4]]
			lin2 = linha[jogada[5]]

			posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)

			normal_dama(tab)

			#AQUI EU FIZ UM LAÇO PARA CONTAR O NUMERO DE PEÇAS
			C = 0
			B = 0
			for i in range(0, 10):
				for j in range(0, 10):
					if tab[i][j] == "o" or tab[i][j] == "O":
						C+=1
					if tab[i][j] == "@" or tab[i][j] == "&":
						B+=1
			qtd_cima = C
			qtd_baixo = B


			#AQUI É PARA CONFERIR SE TEM CONDIÇÃO DE O USUÁRIO JOGAR NOVAMENTE
			if jogador_vez == "B":
				if qtd_cima_anterior != qtd_cima:
					jogador_vez = "B"
				else:
					jogador_vez = "C"
			else:
				if qtd_baixo_anterior != qtd_baixo:
					jogador_vez == "C"
				else:
					jogador_vez = "B"

			print(qtd_cima)
			print(qtd_baixo)
			tabuleiro(tab)

			if qtd_cima == 0:
				print("O vencedor é o usuário de Baixo")
				start = input("Você gostaria de começar de novo? Digite S/s para sim e N/n para não: ")
			if qtd_baixo == 0:
				print("O vencedor é o usuário de Cima")
				start = input("Você gostaria de começar de novo? Digite S/s para sim e N/n para não: ")