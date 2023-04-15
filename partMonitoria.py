num_alunas = int(input())
result = []

for i in range(0, num_alunas):
    nome = input()
    minutos = int(input())
    minutos2 = int(input())
    minutos3 = int(input())
    minutos4 = int(input())

    if minutos >= 120 and minutos2 >= 120 and minutos3 >= 120 and minutos4 >= 120:
        result.append("{} tem monitorias OK! :-)".format(nome))
    else:
        result.append("{} não tem monitorias suficientes :-(".format(nome))

str = " \n".join(result)
print(str)