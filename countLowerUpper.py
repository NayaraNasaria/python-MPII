padrao = input()
padrao_lower = padrao.lower()
linha = input()
linha_lower = linha.lower()

semCapital = linha_lower.count(padrao_lower)
ocorrencia = linha.count(padrao)
print(ocorrencia)
print(semCapital)