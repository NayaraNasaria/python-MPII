pior_estimativa = float(input())
num_ocorrencias = int(input())
ocorrencias = []
contador = 0

for i in range(0, num_ocorrencias):
    ocorrencias.append(float(input()))

for valor in ocorrencias:
    if valor > pior_estimativa:
        contador = contador+1

print(contador)