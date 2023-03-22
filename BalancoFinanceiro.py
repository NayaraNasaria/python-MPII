# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
Alimentacao = []
Moradia = []
Transporte = []
Saude = []
Lazer = []
Salario = []
Prestacao = []
origemInicial=[]
movimentacoes = int(input())
total_renda = 0.00
total_gastos = 0.00

for movimentacoes in range(0, movimentacoes):
    valor = float(input())
    origem = input()
    if valor < 0:
        if origem == "A":
            a = "Alimentação:"
            Alimentacao.append(valor)
            origemInicial.append(origem)
        elif origem == "M":
            m = "Moradia:"
            Moradia.append(valor)
            origemInicial.append(origem)
        elif origem == "T":
            t = "Transporte:"
            Transporte.append(valor)
            origemInicial.append(origem)
        elif origem == "S":
            s = "Saúde:"
            Saude.append(valor)
            origemInicial.append(origem)
        elif origem == "L":
            l = "Lazer:"
            Lazer.append(valor)
            origemInicial.append(origem)
    else:
        if origem == "S":
            sal = "Salário:"
            Salario.append(valor)
            origemInicial.append(origem)
        elif origem == "P":
            p = "Prestação de serviços:"
            Prestacao.append(valor)
            origemInicial.append(origem)
            
total_alimentacao = (sum(filter(lambda x: x < 0, Alimentacao)))
total_moradia = (sum(filter(lambda x: x < 0, Moradia)))
total_transporte = (sum(filter(lambda x: x < 0, Transporte)))
total_saude = (sum(filter(lambda x: x < 0, Saude)))
total_lazer = (sum(filter(lambda x: x < 0, Lazer)))

total_sal = (sum(filter(lambda x: x > 0, Salario)))
total_prestacao = (sum(filter(lambda x: x > 0, Prestacao)))

total_renda = total_sal + total_prestacao
total_gastos = total_alimentacao + total_moradia + total_transporte + total_saude + total_lazer


if total_gastos > total_renda:
    balanco = total_renda - total_gastos
else:
    balanco = total_renda + total_gastos

print("Movimentações")

if "A" in origemInicial:
    print(a, "%.2f" % total_alimentacao)
    
if "M" in origemInicial:
    print(m, "%.2f" % total_moradia)
    
if "T" in origemInicial:
    print(t, "%.2f" % total_transporte)
    
if total_saude < 0:
    print(s,"%.2f" % total_saude)

if "L" in origemInicial:
    print(l, "%.2f" % total_lazer)
    
if total_sal > 0:
    print(sal, "%.2f" % total_sal)
    
if "P" in origemInicial:
    print(p, "%.2f" % total_prestacao)
    
print("Total de Renda:", "%.2f" % total_renda)
print("Total de Gastos:", "%.2f" % total_gastos)
print("Balanço:", "%.2f" % balanco)
