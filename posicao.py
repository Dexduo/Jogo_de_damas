#ESSA É UMA FUNÇÃO PARA CHECAR A VALIDADE DA JOGADA E COMER OUTRA PEÇA
def nova_pos(tab, peca, jogador_vez, lin1, col1, lin2, col2):

	#AQUI SE A PEÇA FOR DAMA EU CHECO A VALIDADE DA JOGADA
	if peca == "dama":

		if jogador_vez == "B":
			#AQUI SE FOR DE BAIXO E FOR PARA FRENTE EM SUA RELAÇÃO
			if lin2<lin1:
				if col2<col1:
					passo = col1
					qtd_inimiga = 0
					for i in range(lin1-1, lin2-1, -1):
						passo-=1
						if tab[i][passo] == "o" or tab[i][passo] == "O":
							qtd_inimiga+=1
							l_pego = i
							c_pego = passo
					if qtd_inimiga == 0:
						tab[lin1][col1] = " "
						tab[lin2][col2] = "&"
					if qtd_inimiga == 1:
						tab[l_pego][c_pego] = " "
						tab[lin1][col1] = " "
						tab[lin2][col2] = "&"
					else:
						print("Jogada invalida")


				if col2>col1:
					passo = col1
					qtd_inimiga = 0
					for i in range(lin1-1, lin2-1, -1):
						passo+=1
						if tab[i][passo] == "o" or tab[i][passo] == "O":
							qtd_inimiga+=1
							l_pego = i
							c_pego = passo
					if qtd_inimiga == 0:
						tab[lin1][col1] = " "
						tab[lin2][col2] = "&"
					if qtd_inimiga == 1:
						tab[l_pego][c_pego] = " "
						tab[lin1][col1] = " "
						tab[lin2][col2] = "&"
					else:
						print("Jogada invalida")

			#AQUI SE FOR DE BAIXO E FOR PARA TRÁS EM SUA RELAÇÃO
			if lin2>lin1:
				if col2<col1:
					passo = col1
					qtd_inimiga = 0
					for i in range(lin1+1, lin2+1):
						passo-=1
						if tab[i][passo] == "o" or tab[i][passo] == "O":
							qtd_inimiga+=1
							l_pego = i
							c_pego = passo
					if qtd_inimiga == 0:
						tab[lin1][col1] = " "
						tab[lin2][col2] = "&"
					if qtd_inimiga == 1:
						tab[l_pego][c_pego] = " "
						tab[lin1][col1] = " "
						tab[lin2][col2] = "&"
					else:
						print("Jogada invalida")


				if col2>col1:
					passo = col1
					qtd_inimiga = 0
					for i in range(lin1+1, lin2+1):
						passo+=1
						if tab[i][passo] == "o" or tab[i][passo] == "O":
							qtd_inimiga+=1
							l_pego = i
							c_pego = passo
					if qtd_inimiga == 0:
						tab[lin1][col1] = " "
						tab[lin2][col2] = "&"
					if qtd_inimiga == 1:
						tab[l_pego][c_pego] = " "
						tab[lin1][col1] = " "
						tab[lin2][col2] = "&"
					else:
						print("Jogada invalida")


		if jogador_vez == "C":
			#AQUI SE FOR DE CIMA E FOR PARA TRÁS EM SUA RELAÇÃO
			if lin2<lin1:
				if col2<col1:
					passo = col1
					qtd_inimiga = 0
					for i in range(lin1-1, lin2-1, -1):
						passo-=1
						if tab[i][passo] == "@" or tab[i][passo] == "&":
							qtd_inimiga+=1
							l_pego = i
							c_pego = passo
					if qtd_inimiga == 0:
						tab[lin1][col1] = " "
						tab[lin2][col2] = "O"
					if qtd_inimiga == 1:
						tab[l_pego][c_pego] = " "
						tab[lin1][col1] = " "
						tab[lin2][col2] = "O"
					else:
						print("Jogada invalida")


				if col2>col1:
					passo = col1
					qtd_inimiga = 0
					for i in range(lin1-1, lin2-1, -1):
						passo+=1
						if tab[i][passo] == "@" or tab[i][passo] == "&":
							qtd_inimiga+=1
							l_pego = i
							c_pego = passo
					if qtd_inimiga == 0:
						tab[lin1][col1] = " "
						tab[lin2][col2] = "O"
					if qtd_inimiga == 1:
						tab[l_pego][c_pego] = " "
						tab[lin1][col1] = " "
						tab[lin2][col2] = "O"
					else:
						print("Jogada invalida")

			#AQUI SE FOR DE BAIXO E FOR PARA FRENTE EM SUA RELAÇÃO
			if lin2>lin1:
				if col2<col1:
					passo = col1
					qtd_inimiga = 0
					for i in range(lin1+1, lin2+1):
						passo-=1
						if tab[i][passo] == "@" or tab[i][passo] == "&":
							qtd_inimiga+=1
							l_pego = i
							c_pego = passo
					if qtd_inimiga == 0:
						tab[lin1][col1] = " "
						tab[lin2][col2] = "O"
					if qtd_inimiga == 1:
						tab[l_pego][c_pego] = " "
						tab[lin1][col1] = " "
						tab[lin2][col2] = "O"
					else:
						print("Jogada invalida")


				if col2>col1:
					passo = col1
					qtd_inimiga = 0
					for i in range(lin1+1, lin2+1):
						passo+=1
						if tab[i][passo] == "@" or tab[i][passo] == "&":
							qtd_inimiga+=1
							l_pego = i
							c_pego = passo
					if qtd_inimiga == 0:
						tab[lin1][col1] = " "
						tab[lin2][col2] = "O"
					if qtd_inimiga == 1:
						tab[l_pego][c_pego] = " "
						tab[lin1][col1] = " "
						tab[lin2][col2] = "O"
					else:
						print("Jogada invalida")




	#AQUI SE A PEÇA FOR NORMAL EU CHECO A VALIDADE DA JOGADA				
	if peca == "normal":

		if jogador_vez=="C":

			if tab[int((lin1+lin2)/2)][int((col1+col2)/2)] == "@" or tab[int((lin1+lin2)/2)][int((col1+col2)/2)] == "&":
				tab[int((lin1+lin2)/2)][int((col1+col2)/2)] = " "
				tab[lin1][col1] = " "
				tab[lin2][col2] = "o" 

			if (lin1-lin2 >= 1 and (col1==col2+1 or col1==col2-1)) or (lin2>lin1+1) or (tab[lin2][col2] != " "):
				print("Jogada invalida") 
			else:
				tab[lin1][col1] = " "
				tab[lin2][col2] = "o"

		if jogador_vez=="B":

			if tab[int((lin1+lin2)/2)][int((col1+col2)/2)] == "o" or tab[int((lin1+lin2)/2)][int((col1+col2)/2)] == "O":
				tab[int((lin1+lin2)/2)][int((col1+col2)/2)] = " "
				tab[lin1][col1] = " "
				tab[lin2][col2] = "@" 

			if (lin2-lin1 >= 1 and (col1==col2+1 or col1==col2-1)) or (lin1>lin2+1) or (tab[lin2][col2] != " "):
				print("Jogada invalida") 
			else:
				tab[lin1][col1] = " "
				tab[lin2][col2] = "@"


