#essa é uma função para exibir o tabuleiro
def tabuleiro(tab):
	print("    A   B   C   D   E   F   G   H   I   J")
	for i in range(0, 10):
		print("  +---+---+---+---+---+---+---+---+---+---+")
		print(i, "| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(tab[i][0], tab[i][1], tab[i][2], tab[i][3], tab[i][4], tab[i][5], tab[i][6], tab[i][7], tab[i][8], tab[i][9]))
	print("  +---+---+---+---+---+---+---+---+---+---+")

#essa é uma função para conferir e atualizar posições no tabuleiro
def nova_pos(tab, jogada):
	coluna = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
	linha = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
	
	if tab[linha[jogada[1]]][coluna[jogada[0]]] == "o":
		if linha[jogada[5]]<=linha[jogada[1]] or tab[linha[jogada[5]]][coluna[jogada[4]]]!=" ":
		 	print("Jogada inválida!!!")
		else:
			tab[linha[jogada[1]]][coluna[jogada[0]]] = " "
			tab[linha[jogada[5]]][coluna[jogada[4]]] = "o"

	if tab[linha[jogada[1]]][coluna[jogada[0]]] == "@":
		if linha[jogada[5]]>=linha[jogada[1]] or tab[linha[jogada[5]]][coluna[jogada[4]]]!=" ":
			print("Jogada inválida!!!")
		else:
			tab[linha[jogada[1]]][coluna[jogada[0]]] = " "
			tab[linha[jogada[5]]][coluna[jogada[4]]] = "@"