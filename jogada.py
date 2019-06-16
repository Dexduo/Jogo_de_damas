from checar import checar_normal_baixo
from checar import checar_normal_cima
from checar import checar_dama_baixo
from checar import checar_dama_cima

def posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada):

	coluna = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
	linha = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

	col1 = coluna[jogada[0]]
	lin1 = linha[jogada[1]]
	col2 = coluna[jogada[4]]
	lin2 = linha[jogada[5]]

	comer = 0

	if tab[lin1][col1] == "@" or tab[lin1][col1] == "o":
		peca = "normal"
	else:
		if tab[lin1][col1] == "&" or tab[lin1][col1] == "O":
			peca = "dama"
		else:
			peca = "invalida"

	if jogador_vez != "C" and jogador_vez != "B":
		print("Jogada Invalida1")
		jogador_vez = input("Diga quem vai jogar: ")
		posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)

	else:
		#IREI CHECAR SE A PEÇA É NORMAL
		if peca == "normal":
			#AQUI SE A PEÇA FOR NORMAL E TENTAR PULAR MAIS DE 2 CASAS É INVALIDA
			if int(((lin2-lin1)**2)**(1/2))>2 or int(((col2-col1)**2)**(1/2))>2 or tab[lin2][col2] != " ":
				print("Jogada Invalida2")
				jogada = input("Refaça sua jogada: ")
				posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)
			else:
	 		#SE NÃO PULAR MAIS DE DUAS CASAS EU VEJO QUEM VAI JOGAR AGORA
	 			#SE QUEM JOGAR FOR AS NORMAIS DE BAIXO:
				if jogador_vez == "B":
					
					comer = checar_normal_baixo(tab, comer)
					if comer == 0:
						comer = checar_dama_baixo(tab, comer)
					
					lin_chance = int(((( (lin1)**2)**(1/2) ) + (( (lin2)**2)**(1/2) ))/2)
					col_chance = int(((( (col1)**2)**(1/2) ) + (( (col2)**2)**(1/2) ))/2)
					#SE TIVER ADVERSARIAS AO REDOR EU CHECO SE A JOGADA PASSOU POR CIMA DA PEÇA ADVERSÁRIA
					if comer == 1:
						if tab[lin_chance][col_chance] != "o" and tab[lin_chance][col_chance] != "O":
							print("Jogada invalida3")
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
							print("Jogada Invalida4")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)
						else:
							#SE NÃO PULOU MAIS DE UMA CASA EU ATUALIZO O TABULEIRO
							tab[lin2][col2] = tab[lin1][col1]
							tab[lin1][col1] = " "


				#SE QUEM JOGAR FOR AS NORMAIS DE CIMA:
				if jogador_vez == "C":
					
					comer = checar_normal_cima(tab, comer)
					if comer == 0:
						comer = checar_dama_cima(tab, comer)

					
					lin_chance = int(((( (lin1)**2)**(1/2) ) + (( (lin2)**2)**(1/2) ))/2)
					col_chance = int(((( (col1)**2)**(1/2) ) + (( (col2)**2)**(1/2) ))/2)
					#SE TIVER ADVERSARIAS AO REDOR EU CHECO SE A JOGADA PASSOU POR CIMA DA PEÇA ADVERSÁRIA
					if comer == 1:
						if tab[lin_chance][col_chance] != "@" and tab[lin_chance][col_chance] != "&":
							print("Jogada invalida5")
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
							print("Jogada Invalida6")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)
						else:
							#SE NÃO PULOU MAIS DE UMA CASA EU ATUALIZO O TABULEIRO
							tab[lin2][col2] = tab[lin1][col1]
							tab[lin1][col1] = " "

		


		#IREI CHECAR SE A PEÇA É DAMA
		if peca == "dama":
			lin_inimiga = -1
			col_inimiga = -1
			qtdd_inimiga = 0
			qtdd_aliados = 0
			#SE QUEM FOR JOGAR FOR AS DAMAS DE BAIXO:
			if jogador_vez == "B":
				comer = checar_dama_baixo(tab, comer)
				if comer == 0:
					comer = checar_normal_baixo(tab, comer)
				#SE PUDER COMER ALGUMA:
				if comer == 1:
					if lin2<lin1 and col2<col1:
						for i in range(1, int(((lin2-lin1)**2)*1/2)):
							if tab[lin1-i][col1-i] == "o" or tab[lin1-i][col1-i] == "O":
								if qtdd_inimiga == 0:
									qtdd_inimiga += 1
									lin_inimiga = lin1-i
									col_inimiga = col1-i
							if tab[lin1-i][col1-i] == "@" or tab[lin1-i][col1-i] == "&":
								qtdd_aliados+=1
								lin_aliado = lin1-i
								col_aliado = col1-i
						if qtdd_inimiga == 1 and tab[lin2][col2] == " " and qtdd_aliados == 0:
							tab[lin2][col2] = "&"
							tab[lin1][col1] = " "
							tab[lin_inimiga][col_inimiga] = " "
						else:
							print("Jogada Invalida7")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)

					if lin2<lin1 and col2>col1:
						for i in range(1, int(((lin2-lin1)**2)*1/2)):
							if tab[lin1-i][col1+i] == "o" or tab[lin1-i][col1+i] == "O":
								if qtdd_inimiga == 0:
									qtdd_inimiga += 1
									lin_inimiga = lin1-i
									col_inimiga = col1-i
								if tab[lin1-i][col1+i] == "@" or tab[lin1-i][col1+i] == "&":
									qtdd_aliados+=1
						if qtdd_inimiga == 1 and tab[lin2][col2] == " " and qtdd_aliados == 0:
							tab[lin2][col2] = "&"
							tab[lin1][col1] = " "
							tab[lin_inimiga][col_inimiga] = " "
						else:
							print("Jogada Invalida8")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)

					if lin2>lin1 and col2<col1:
						for i in range(1, int(((lin2-lin1)**2)*1/2)):
							if tab[lin1+i][col1-i] == "o" or tab[lin1+i][col1-i] == "O":
								if qtdd_inimiga == 0:
									qtdd_inimiga += 1
									lin_inimiga = lin1-i
									col_inimiga = col1-i
								if tab[lin1+i][col1-i] == "@" or tab[lin1+i][col1-i] == "&":
									qtdd_aliados+=1
						if qtdd_inimiga == 1 and tab[lin2][col2] == " " and qtdd_aliados == 0:
							tab[lin2][col2] = "&"
							tab[lin1][col1] = " "
							tab[lin_inimiga][col_inimiga] = " "
						else:
							print("Jogada Invalida9")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)

					if lin2>lin1 and col2>col1:
						for i in range(1, int(((lin2-lin1)**2)*1/2)):
							if tab[lin1+i][col1+i] == "o" or tab[lin1+i][col1+i] == "O":
								if qtdd_inimiga == 0:
									qtdd_inimiga += 1
									lin_inimiga = lin1-i
									col_inimiga = col1-i
								if tab[lin1+i][col1+i] == "@" or tab[lin1+i][col1+i] == "&":
									qtdd_aliados+=1
						if qtdd_inimiga == 1 and tab[lin2][col2] == " " and qtdd_aliados == 0:
							tab[lin2][col2] = "&"
							tab[lin1][col1] = " "
							tab[lin_inimiga][col_inimiga] = " "
						else:
							print("Jogada Invalida10")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)

				#SE NÃO PUDER COMER NENHUMA:
				else:
					tab[lin2][col2] = tab[lin1][col1]
					tab[lin1][col1] = " "
				print(comer)


			#SE QUEM FOR JOGAR FOR AS DAMAS DE CIMA:
			if jogador_vez == "C":
				comer = checar_dama_cima(tab, comer)
				if comer == 0:
					comer = checar_normal_cima(tab, comer)
				#SE PUDER COMER ALGUMA:
				if comer == 1:

					if lin2<lin1 and col2<col1:
						for i in range(1, int(((lin2-lin1)**2)*1/2)):
							if tab[lin1-i][col1-i] == "@" or tab[lin1-i][col1-i] == "&":
								if qtdd_inimiga == 0:
									qtdd_inimiga += 1
									lin_inimiga = lin1-i
									col_inimiga = col1-i
							if tab[lin1-i][col1-i] == "o" or tab[lin1-i][col1-i] == "O":
								qtdd_aliados += 1
						if qtdd_inimiga == 1 and tab[lin2][col2] == " " and qtdd_aliados == 0:
							tab[lin2][col2] = "O"
							tab[lin1][col1] = " "
							tab[lin_inimiga][col_inimiga] = " "
						else:
							print("Jogada Invalida11")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)

					if lin2<lin1 and col2>col1:
						for i in range(1, int(((lin2-lin1)**2)*1/2)):
							if tab[lin1-i][col1+i] == "@" or tab[lin1-i][col1+i] == "&":
								if qtdd_inimiga == 0:
									qtdd_inimiga += 1
									lin_inimiga = lin1-i
									col_inimiga = col1-i
							if tab[lin1-i][col1+i] == "o" or tab[lin1-i][col1+i] == "O":
								qtdd_aliados += 1
						if qtdd_inimiga == 1 and tab[lin2][col2] == " " and qtdd_aliados == 0:
							tab[lin2][col2] = "O"
							tab[lin1][col1] = " "
							tab[lin_inimiga][col_inimiga] = " "
						else:
							print("Jogada Invalida12")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)

					if lin2>lin1 and col2<col1:
						for i in range(1, int(((lin2-lin1)**2)*1/2)):
							if tab[lin1+i][col1-i] == "@" or tab[lin1+i][col1-i] == "&":
								if qtdd_inimiga == 0:
									qtdd_inimiga += 1
									lin_inimiga = lin1-i
									col_inimiga = col1-i
							if tab[lin1+i][col1-i] == "o" or tab[lin1+i][col1-i] == "O":
								qtdd_aliados += 1
						if qtdd_inimiga == 1 and tab[lin2][col2] == " " and qtdd_aliados == 0:
							tab[lin2][col2] = "O"
							tab[lin1][col1] = " "
							tab[lin_inimiga][col_inimiga] = " "
						else:
							print("Jogada Invalida13")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)

					if lin2>lin1 and col2>col1:
						for i in range(1, int(((lin2-lin1)**2)*1/2)):
							if tab[lin1+i][col1+i] == "@" or tab[lin1+i][col1+i] == "&":
								if qtdd_inimiga == 0:
									qtdd_inimiga += 1
									lin_inimiga = lin1-i
									col_inimiga = col1-i
							if tab[lin1+i][col1+i] == "o" or tab[lin1+i][col1+i] == "O":
								qtdd_aliados += 1
						if qtdd_inimiga == 1 and tab[lin2][col2] == " " and qtdd_aliados == 0:
							tab[lin2][col2] = "O"
							tab[lin1][col1] = " "
							tab[lin_inimiga][col_inimiga] = " "
						else:
							print("Jogada Invalida14")
							jogada = input("Refaça sua jogada: ")
							posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)

				#SE NÃO PUDER COMER NENHUMA:
				else:
					tab[lin2][col2] = tab[lin1][col1]
					tab[lin1][col1] = " "




		if peca == "invalida":
			print("Jogada Invalida15")
			jogada = input("Refaça sua jogada: ")
			posicao(peca, lin1, col1, lin2, col2, tab, jogador_vez, jogada)





