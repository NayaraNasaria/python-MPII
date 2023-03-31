valor = [int(i) for i in input().split()]

for i in valor:
  linha = ''
  for a in range(i):
    linha += '*'
  print(linha)