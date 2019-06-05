#essa é uma função para exibir o tabuleiro
def tabuleiro(tab):
	print("    A   B   C   D   E   F   G   H   I   J")
	for i in range(0, 10):
		print("  +---+---+---+---+---+---+---+---+---+---+")
		print(i, "| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(tab[i][0], tab[i][1], tab[i][2], tab[i][3], tab[i][4], tab[i][5], tab[i][6], tab[i][7], tab[i][8], tab[i][9]))
	print("  +---+---+---+---+---+---+---+---+---+---+")
