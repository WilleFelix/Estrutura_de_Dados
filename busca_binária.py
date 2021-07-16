from datetime import datetime
start_time = datetime.now() 

def busca_binaria(lista,elemento):
	inicio = 0
	fim = len(lista)-1
	encontrado = False

	while inicio <= fim and not encontrado:
		meio = (inicio + fim) // 2
		if lista[meio] == elemento:
			encontrado = True
		else:
			if elemento < lista[meio]:
				fim = meio - 1
			else:
				inicio = meio+1 

	return encontrado



print(busca_binaria(range(0,101),2))


end_time = datetime.now()
print("Duracao: {}".format(end_time-start_time))
