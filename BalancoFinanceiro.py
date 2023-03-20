movimentacoes = int(input())

for movimentacoes in range(0, movimentacoes, 1):
    valor = float(input())

    if valor < 0:
        origemDespesa = input()
        if origemDespesa == "A":
            print("Alimentação:", "%.2f" % valor)
        elif origemDespesa == "M":
            print("Moradia", "%.2f" % valor)
        elif origemDespesa == "T":
            print("Transporte:", "%.2f" % valor)
        elif origemDespesa == "L":
            print("Lazer:", "%.2f" % valor)
        elif origemDespesa == "S":
            print("Saúde:", "%.2f" % valor)
    else:
        origemDespesa = input()

        if origemDespesa == "S":
            print("Salário:", "%.2f" % valor)
        elif origemDespesa == "P":
            print("Prestação de serviços:", "%.2f" % valor)