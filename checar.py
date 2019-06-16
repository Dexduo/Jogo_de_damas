#essa é uma função para checar a chance de comida

#ESSA FUNÇÃO PARA CHECAR PARA AS NORMAIS
def checar_normal_baixo(tab, comer):
	#AQUI FIZ UM LAÇO PRA CHECAR SE TEM PECAS ADVERSÁRIAS AO REDOR	

	for k in range(0, 10):
		for h in range(0, 10):
			if tab[k][h] == "@":
				#TEVE MUITA COISA AQUI POIS TIVE QUE FAZER CASOS ESPECÍFICOS PARA OS EXTREMOS DO TABULEIRO
					if k>=2 and k<=7 and h>=2 and h<=7:
						for i in range(-1, 2, 2):
							for j in range(-1, 2, 2):
								if (tab[k+i][h+j] == "o" or tab[k+i][h+j] == "O") and (tab[k+(2*i)][h+(2*j)] == " "):
									comer = 1
					
					if k <= 1 and h>=2 and h<=7:
						i = 1
						for j in range(-1, 2, 2):
							if (tab[k+i][h+j] == "o" or tab[k+i][h+j] == "O") and (tab[k+(2*i)][h+(2*j)] == " "):
								comer = 1

					if k >= 8 and h>=2 and h<=7:
						i = -1
						for j in range(-1, 2, 2):
							if (tab[k+i][h+j] == "o" or tab[k+i][h+j] == "O") and (tab[k+(2*i)][h+(2*j)] == " "):
								comer = 1

					if h <= 1 and k>=2 and k<=7:
						j = 1
						for i in range(-1, 2, 2):
							if (tab[k+i][h+j] == "o" or tab[k+i][h+j] == "O") and (tab[k+(2*i)][h+(2*j)] == " "):
								comer = 1

					if h >= 8 and k>=2 and k<=7:
						j = -1
						for i in range(-1, 2, 2):
							if (tab[k+i][h+j] == "o" or tab[k+i][h+j] == "O") and (tab[k+(2*i)][h+(2*j)] == " "):
								comer = 1

					if (k==0 and h==1) or (k==1 and h==0):
						i = 1
						j = 1
						if (tab[k+i][h+j] == "o" or tab[k+i][h+j] == "O") and (tab[k+(2*i)][h+(2*j)] == " "):
							comer = 1

					if (k==8 and h==1) or (k==9 and h==0):
						i = -1
						j = 1
						if (tab[k+i][h+j] == "o" or tab[k+i][h+j] == "O") and (tab[k+(2*i)][h+(2*j)] == " "):
							comer = 1

					if (k==0 and h==9) or (k==1 and h==8):
						i = 1
						j = -1
						if (tab[k+i][h+j] == "o" or tab[k+i][h+j] == "O") and (tab[k+(2*i)][h+(2*j)] == " "):
							comer = 1

					if (k==9 and h==8) or (k==8 and h==9):
						i = -1
						j = -1
						if (tab[k+i][h+j] == "o" or tab[k+i][h+j] == "O") and (tab[k+(2*i)][h+(2*j)] == " "):
							comer = 1
	return comer

def checar_normal_cima(tab, comer):
	for k in range(0, 10):
		for h in range(0, 10):
			if tab[k][h] == "o":
				#TEVE MUITA COISA AQUI POIS TIVE QUE FAZER CASOS ESPECÍFICOS PARA OS EXTREMOS DO TABULEIRO
					if k>=2 and k<=7 and h>=2 and h<=7:
						for i in range(-1, 2, 2):
							for j in range(-1, 2, 2):
								if (tab[k+i][h+j] == "@" or tab[k+i][h+j] == "&") and (tab[k+(2*i)][h+(2*j)] == " "):
									comer = 1
					
					if k <= 1 and h>=2 and h<=7:
						i = 1
						for j in range(-1, 2, 2):
							if (tab[k+i][h+j] == "@" or tab[k+i][h+j] == "&") and (tab[k+(2*i)][h+(2*j)] == " "):
								comer = 1

					if k >= 8 and h>=2 and h<=7:
						i = -1
						for j in range(-1, 2, 2):
							if (tab[k+i][h+j] == "@" or tab[k+i][h+j] == "&") and (tab[k+(2*i)][h+(2*j)] == " "):
								comer = 1

					if h <= 1 and k>=2 and k<=7:
						j = 1
						for i in range(-1, 2, 2):
							if (tab[k+i][h+j] == "@" or tab[k+i][h+j] == "&") and (tab[k+(2*i)][h+(2*j)] == " "):
								comer = 1

					if h >= 8 and k>=2 and k<=7:
						j = -1
						for i in range(-1, 2, 2):
							if (tab[k+i][h+j] == "@" or tab[k+i][h+j] == "&") and (tab[k+(2*i)][h+(2*j)] == " "):
								comer = 1

					if (k==0 and h==1) or (k==1 and h==0):
						i = 1
						j = 1
						if (tab[k+i][h+j] == "@" or tab[k+i][h+j] == "&") and (tab[k+(2*i)][h+(2*j)] == " "):
							comer = 1

					if (k==8 and h==1) or (k==9 and h==0):
						i = -1
						j = 1
						if (tab[k+i][h+j] == "@" or tab[k+i][h+j] == "&") and (tab[k+(2*i)][h+(2*j)] == " "):
							comer = 1

					if (k==0 and h==9) or (k==1 and h==8):
						i = 1
						j = -1
						if (tab[k+i][h+j] == "@" or tab[k+i][h+j] == "&") and (tab[k+(2*i)][h+(2*j)] == " "):
							comer = 1

					if (k==9 and h==8) or (k==8 and h==9):
						i = -1
						j = -1
						if (tab[k+i][h+j] == "@" or tab[k+i][h+j] == "&") and (tab[k+(2*i)][h+(2*j)] == " "):
							comer = 1


	return comer

#ESSA FUNÇÃO PARA CHECAR PARA AS DAMAS
def checar_dama_baixo(tab, comer):

	for k in range(0, 10):
		for h in range(0, 10):


			if tab[k][h] == "&":
				if k<=4 and h<=4:
					#checar superior esquerdo:
					for i in range(0, h):
						if k-i-1 >= 0 :
							if (tab[k-i][h-i] == "o" or tab[k-i][h-i] == "O") and tab[k-i-1][h-i-1] == " ":
								comer = 1
					#checar superior direito:
					for i in range(0, k):
						if (tab[k-i][h+i] == "o" or tab[k-i][h+i] == "O") and tab[k-i-1][h+i+1] == " ":
							comer = 1
					#checar inferior esquerdo:
					for i in range(0, h):
						if (tab[k+i][h-i] == "o" or tab[k+i][h-i] == "O") and tab[k+i+1][h-i-1] == " ":
							comer = 1
					#checar inferior direito:
					lin = k+1
					col = h+1
					while lin<9 or col<9:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin+1][col+1] == " ":
							comer = 1
						lin += 1
						col += 1


				if k<=4 and h>=5:
					#checar superior esquerdo:
					for i in range(0, k):
						if (tab[k-i][h-i] == "o" or tab[k-i][h-i] == "O") and tab[k-i-1][h-i-1] == " ":
								comer = 1
					#checar superior direito:
					lin = k-1
					col = h+1
					while lin>0 or col<9:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin-1][col+1] == " ":
							comer = 1
						lin -= 1
						col += 1
					#canto inferior esquerdo:
					lin = k+1
					col = h-1
					while lin<9 or col>0:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin+1][col-1] == " ":
							comer = 1
						lin += 1
						col -= 1
					#canto inferior direito:
					lin = k+1
					col = h+1
					while col<9:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin+1][col-1] == " ":
							comer = 1
						lin += 1
						col += 1


				if k>=5 and h<=4:
					#canto superior esquerdo:
					lin = k-1
					col = h-1
					while col>0:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin+1][col-1] == " ":
							comer = 1
						lin -= 1
						col -= 1
					#canto superior direito:
					lin = k-1
					col = h+1
					while lin>0 or col<9:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin-1][col+1] == " ":
							comer = 1
						lin -= 1
						col += 1
					#canto inferior esquerdo:
					lin = k+1
					col = h-1
					while lin<9 or col>0:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin+1][col-1] == " ":
							comer = 1
						lin += 1
						col -= 1
					#canto inferior direito:
					lin = k+1
					col = h+1
					while lin<9:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin+1][col+1] == " ":
							comer = 1
						lin += 1
						col += 1


				if k>=5	and h>=5:
					#canto superior esquerdo:
					lin = k-1
					col = h-1
					while lin>0 or col>0:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin-1][col-1] == " ":
							comer = 1
						lin -= 1
						col -= 1
					#canto superior direito:
					lin = k-1
					col = h+1
					while col<9:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin-1][col+1] == " ":
							comer = 1
						lin -= 1
						col += 1
					#canto inferior esquerdo:
					lin = k+1
					col = h-1
					while lin<9:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin+1][col-1] == " ":
							comer = 1
						lin += 1
						col -= 1
					#canto inferior direito:
					lin = k+1
					col = h+1
					while lin<9 or col<9:
						if (tab[lin][col] == "o" or tab[lin][col] == "O") and tab[lin+1][col+1] == " ":
							comer = 1
						lin += 1
						col += 1

	return comer

def checar_dama_cima(tab, comer):
	for k in range(0, 10):
		for h in range(0, 10):


			if tab[k][h] == "O":
				if k<=4 and h<=4:
					#checar superior esquerdo:
					for i in range(0, h):
						if k-i-1 >= 0 :
							if (tab[k-i][h-i] == "@" or tab[k-i][h-i] == "&") and tab[k-i-1][h-i-1] == " ":
								comer = 1
					#checar superior direito:
					for i in range(0, k):
						if (tab[k-i][h+i] == "@" or tab[k-i][h+i] == "&") and tab[k-i-1][h+i+1] == " ":
							comer = 1
					#checar inferior esquerdo:
					for i in range(0, h):
						if (tab[k+i][h-i] == "@" or tab[k+i][h-i] == "&") and tab[k+i+1][h-i-1] == " ":
							comer = 1
					#checar inferior direito:
					lin = k+1
					col = h+1
					while lin<9 or col<9:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin+1][col+1] == " ":
							comer = 1
						lin += 1
						col += 1


				if k<=4 and h>=5:
					#checar superior esquerdo:
					for i in range(0, k):
						if (tab[k-i][h-i] == "@" or tab[k-i][h-i] == "&") and tab[k-i-1][h-i-1] == " ":
								comer = 1
					#checar superior direito:
					lin = k-1
					col = h+1
					while lin>0 or col<9:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin-1][col+1] == " ":
							comer = 1
						lin -= 1
						col += 1
					#canto inferior esquerdo:
					lin = k+1
					col = h-1
					while lin<9 or col>0:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin+1][col-1] == " ":
							comer = 1
						lin += 1
						col -= 1
					#canto inferior direito:
					lin = k+1
					col = h+1
					while col<9:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin+1][col-1] == " ":
							comer = 1
						lin += 1
						col += 1


				if k>=5 and h<=4:
					#canto superior esquerdo:
					lin = k-1
					col = h-1
					while col>0:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin+1][col-1] == " ":
							comer = 1
						lin -= 1
						col -= 1
					#canto superior direito:
					lin = k-1
					col = h+1
					while lin>0 or col<9:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin-1][col+1] == " ":
							comer = 1
						lin -= 1
						col += 1
					#canto inferior esquerdo:
					lin = k+1
					col = h-1
					while lin<9 or col>0:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin+1][col-1] == " ":
							comer = 1
						lin += 1
						col -= 1
					#canto inferior direito:
					lin = k+1
					col = h+1
					while lin<9:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin+1][col+1] == " ":
							comer = 1
						lin += 1
						col += 1


				if k>=5	and h>=5:
					#canto superior esquerdo:
					lin = k-1
					col = h-1
					while lin>0 or col>0:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin-1][col-1] == " ":
							comer = 1
						lin -= 1
						col -= 1
					#canto superior direito:
					lin = k-1
					col = h+1
					while col<9:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin-1][col+1] == " ":
							comer = 1
						lin -= 1
						col += 1
					#canto inferior esquerdo:
					lin = k+1
					col = h-1
					while lin<9:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin+1][col-1] == " ":
							comer = 1
						lin += 1
						col -= 1
					#canto inferior direito:
					lin = k+1
					col = h+1
					while lin<9 or col<9:
						if (tab[lin][col] == "@" or tab[lin][col] == "&") and tab[lin+1][col+1] == " ":
							comer = 1
						lin += 1
						col += 1


	return comer