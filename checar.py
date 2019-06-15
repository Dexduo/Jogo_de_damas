#essa é uma função para checar a chance de comida
def checar_normal(tab, comer):
	comer = 0
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


def checar_dama():
	return 0