from checar import checar
def posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada):

	coluna = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
	linha = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

	col1 = coluna[jogada[0]]
	lin1 = linha[jogada[1]]
	col2 = coluna[jogada[4]]
	lin2 = linha[jogada[5]]

	conf = 1
	comer = 0

	if jogador_vez != "C" and jogador_vez != "B":
		jogador_vez = input("Usuário invalido, quem vai jogar agora?: ")
		posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)

	else:
		#PRIMEIRAMENTE IREI CHECAR SE A PEÇA É NORMAL
		if peca == "normal":
			#AQUI SE A PEÇA FOR NORMAL E TENTAR PULAR MAIS DE 2 CASAS É INVALIDA
			if int(((lin2-lin1)**2)**(1/2))>2 or int(((col2-col1)**2)**(1/2))>2 or tab[lin2][col2] != " ":
				print("Jogada Invalida")
				jogada = input("Refaça sua jogada: ")
				posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)
			else:
	 		#SE NÃO PULAR MAIS DE DUAS CASAS EU VEJO QUEM VAI JOGAR AGORA
	 			#SE QUEM JOGAR FOR AS NORMAIS DE BAIXO:
				if jogador_vez == "B":
					
					comer = checar(tab, comer)
					
					lin_chance = int(((( (lin1)**2)**(1/2) ) + (( (lin2)**2)**(1/2) ))/2)
					col_chance = int(((( (col1)**2)**(1/2) ) + (( (col2)**2)**(1/2) ))/2)
					#SE TIVER ADVERSARIAS AO REDOR EU CHECO SE A JOGADA PASSOU POR CIMA DA PEÇA ADVERSÁRIA
					if comer == 1:
						if tab[lin_chance][col_chance] != "o" and tab[lin_chance][col_chance] != "O":
							print("Jogada invalida")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)
						else:
							#SE ELA PASSOU POR CIMA (COMEU) EU ATUALIZO O TABULEIRO
							tab[lin2][col2] = tab[lin1][col1]
							tab[lin_chance][col_chance] = " "
							tab[lin1][col1] = " "

					#SE NÃO TIVER PEÇAS ADVERŚÁRIAS AO REDOR EU CHECO SE ELE TENTOU PULAR MAIS DE UMA CASA
					else:
						if (int(((lin2-lin1)**2)**(1/2))!=1 or int(((col2-col1)**2)**(1/2))!=1) or lin2>lin1:
							print("Jogada Invalida")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)
						else:
							#SE NÃO PULOU MAIS DE UMA CASA EU ATUALIZO O TABULEIRO
							tab[lin2][col2] = tab[lin1][col1]
							tab[lin1][col1] = " "


				#SE QUEM JOGAR FOR AS NORMAIS DE CIMA:
				if jogador_vez == "C":
					
					comer = checar(tab, comer)
					
					lin_chance = int(((( (lin1)**2)**(1/2) ) + (( (lin2)**2)**(1/2) ))/2)
					col_chance = int(((( (col1)**2)**(1/2) ) + (( (col2)**2)**(1/2) ))/2)
					#SE TIVER ADVERSARIAS AO REDOR EU CHECO SE A JOGADA PASSOU POR CIMA DA PEÇA ADVERSÁRIA
					if comer == 1:
						if tab[lin_chance][col_chance] != "@" and tab[lin_chance][col_chance] != "&":
							print("Jogada invalida")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)
						else:
							#SE ELA PASSOU POR CIMA (COMEU) EU ATUALIZO O TABULEIRO
							tab[lin2][col2] = tab[lin1][col1]
							tab[lin_chance][col_chance] = " "
							tab[lin1][col1] = " "

					#SE NÃO TIVER PEÇAS ADVERŚÁRIAS AO REDOR EU CHECO SE ELE TENTOU PULAR MAIS DE UMA CASA
					else:
						if (int(((lin2-lin1)**2)**(1/2))!=1 or int(((col2-col1)**2)**(1/2))!=1) or lin2<lin1:
							print("Jogada Invalida")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)
						else:
							#SE NÃO PULOU MAIS DE UMA CASA EU ATUALIZO O TABULEIRO
							tab[lin2][col2] = tab[lin1][col1]
							tab[lin1][col1] = " "





