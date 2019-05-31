def comer(tab, jogada):
	coluna = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
	linha = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

	if tab[linha[jogada[1]]][coluna[jogada[0]]] == "o":
		if (linha[jogada[1]]-2==linha[jogada[5]] and coluna[jogada[0]]-2==coluna[jogada[4]]):
			if tab[linha[jogada[1]]-1][coluna[jogada[0]]-1] == "@":
				tab[linha[jogada[1]]-1][coluna[jogada[0]]-1] = " "

		if (linha[jogada[1]]-2==linha[jogada[5]] and coluna[jogada[0]]+2==coluna[jogada[4]]):
			if tab[linha[jogada[1]]-1][coluna[jogada[0]]+1] == "@":
				tab[linha[jogada[1]]-1][coluna[jogada[0]]+1] = " "

		if (linha[jogada[1]]+2==linha[jogada[5]] and coluna[jogada[0]]-2==coluna[jogada[4]]):
			if tab[linha[jogada[1]]+1][coluna[jogada[0]]-1] == "@":
				tab[linha[jogada[1]]+1][coluna[jogada[0]]-1] = " "

		if (linha[jogada[1]]+2==linha[jogada[5]] and coluna[jogada[0]]+2==coluna[jogada[4]]):
			# if tab[linha[jogada[1]]+1][coluna[jogada[0]]+1] == "@":
			# 	tab[linha[jogada[1]]+1][coluna[jogada[0]]+1] = " "
			print("Ok")
	else:
		print("deu ruim!!!")