from datetime import datetime

tempo_início = datetime.now()

def busca_sequencial(lista_vetores,n):
    for i in range(len(lista_vetores)):
        if lista_vetores[i] == n:
            return True
    else:
        return False

print(busca_sequencial(range(0,101),2))



tempo_final= datetime.now()

print('Duração: {}'.format(tempo_início - tempo_final))
