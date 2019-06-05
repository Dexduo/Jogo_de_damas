def nova_pos(tab, peca, jogador_vez, lin1, col1, lin2, col2):
	coluna = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
	linha = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

	if peca == "normal":
		if jogador_vez=="C":
			if (lin1-lin2 >= 1 and (col1==col2+1 or col1==col2-1)) or (lin2>lin1+1) or (tab[lin2][col2] != " "):
				print("Jogada invalida") 
			else:
				tab[lin1][col1] = " "
				tab[lin2][col2] = "o"

		if jogador_vez=="B":
			if (lin1-lin2 >= -1 and (col1==col2+1 or col1==col2-1)) or (lin1>lin2+1) or (tab[lin2][col2] != " "):
				print("Jogada invalida") 
			else:
				tab[lin1][col1] = " "
				tab[lin2][col2] = "@"

		

