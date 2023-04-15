carta = []
for i in range(3):
    carta.append(input())

manilhas = ['4Paus', '7Copas', 'AEspadas', '7Ouros']

contador = 0

for cartas in carta:
    for manilha in manilhas:
        if cartas == manilha:
            contador = contador + 1
print(contador)