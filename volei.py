time1 = input()
time2 = input()
s_pontos = input()
pontos = s_pontos.split()

lista_pontos = []

for i in pontos:
    convert = int(i)
    lista_pontos.append(convert)

pontos_time = [
    lista_pontos[0],
    lista_pontos[1]
]

i_time = lista_pontos[2]
pontos_time[i_time-1] += 1

print(time1, pontos_time[0])
print(time2, pontos_time[1])