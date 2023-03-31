valor = [int(i) for i in input().split()]

if valor.__contains__(0):
    print(".")
else:
    for i in valor:
      linha = ''
      for j in range(i):
        linha += '*'
      print(linha)