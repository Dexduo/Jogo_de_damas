def nova_pos(tab, peca, jogador_vez, lin1, col1, lin2, col2, qtd_cima, qtd_baixo):

	coluna = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
	linha = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}


	if peca == "dama":

		if jogador_vez == "B":
			if lin2<lin1:
				if col2<col1:
					passo = col1
					qtd_inimiga = 0
					for i in range(lin1-1, lin2-1, -1):
						passo-=1
						if tab[i][passo] == "o":
							print("pegou")
							qtd_inimiga+=1
							l_pego = i
							c_pego = passo
						else:
							print("Nao pegou")
					if qtd_inimiga == 1:
						tab[l_pego][c_pego] = " "
						qtd_baixo-=1
						tab[lin2][col2] = "&"
					else:
						print("Jogada invalida")
					
	if peca == "normal":

		if jogador_vez=="C":

			if (lin1-lin2 >= 1 and (col1==col2+1 or col1==col2-1)) or (lin2>lin1+1) or (tab[lin2][col2] != " "):
				print("Jogada invalida") 
			else:
				tab[lin1][col1] = " "
				tab[lin2][col2] = "o"

		if jogador_vez=="B":

			if (lin2-lin1 >= 1 and (col1==col2+1 or col1==col2-1)) or (lin1>lin2+1) or (tab[lin2][col2] != " "):
				print("Jogada invalida") 
			else:
				tab[lin1][col1] = " "
				tab[lin2][col2] = "@"


	# if peca == "dama":

	# 	if tab[lin2][col2] != " ":
	# 		print("Jogada invalida")

	# 	if jogador_vez == "C":
	# 		if lin2>lin1:
	# 			if col2>col1:
	# 				teste = col1
	# 				peca_inimiga = 0
	# 				for i in range(lin1+1, lin2+1):
	# 					if tab[i][teste] == "o" or tab[i][teste] == "O":
	# 						print("Jogada invalida")
	# 					if tab[i][teste] == "@" or tab[i][teste] == "&":
	# 						peca_inimiga+=1
	# 					teste+=1
	# 				if peca_inimiga>1:
	# 					print("Jogada invalida")

	# 			if col2<col1:
	# 				teste = col1
	# 				peca_inimiga = 0
	# 				for i in range(lin1+1, lin2+1):
	# 					if tab[i][teste] == "o" or tab[i][teste] == "O":
	# 						print("Jogada invalida")
	# 					if tab[i][teste] == "@" or tab[i][teste] == "&":
	# 						peca_inimiga+=1
	# 					teste-=1
	# 				if peca_inimiga>1:
	# 					print("Jogada invalida")

	# 		if lin2<lin1:
	# 			if col2>col1:
	# 				teste = col1
	# 				peca_inimiga = 0
	# 				for i in range(lin1+1, lin2+2, -1):
	# 					if tab[i][teste] == "o" or tab[i][teste] == "O":
	# 						print("Jogada invalida")
	# 					if tab[i][teste] == "@" or tab[i][teste] == "&":
	# 						peca_inimiga+=1
	# 					teste+=1
	# 				if peca_inimiga>1:
	# 					print("Jogada invalida")

	# 			if col2<col1:
	# 				teste = col1
	# 				peca_inimiga = 0
	# 				for i in range(lin1+1, lin2+2, -1):
	# 					if tab[i][teste] == "o" or tab[i][teste] == "O":
	# 						print("Jogada invalida")
	# 					if tab[i][teste] == "@" or tab[i][teste] == "&":
	# 						peca_inimiga+=1
	# 					teste-=1
	# 				if peca_inimiga>1:
	# 					print("Jogada invalida")











