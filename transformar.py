#ESSA FUNÇÃO VAI TRANSFORMAR A PEÇA NORMAL EM DAMA CASO CHEGUE AO OUTRO LADO DO TABULEIRO
def normal_dama(tab):
	for i in range(0, 10):
		if tab[9][i] == "o":
			tab[9][i] = "O"

		if tab[0][i] == "@":
			tab[0][i] = "&"