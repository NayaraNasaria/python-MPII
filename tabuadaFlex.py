valor1 = int(input()) #tabuada q eu quero
valor2 = int(input()) #a partir de qual
valor3 = int(input()) # Até
i = 0

print("Tabuada do",valor1,"de", valor2, "até", valor3)

for i in range(valor2, valor3+1):
    tabuada = valor1 * i
    print(valor1, "x", i, "=", tabuada)
