cpf = input()
chars = '.-'

if cpf.__contains__(".") or cpf.__contains__("-"):
    semcaracter = cpf.translate(str.maketrans('', '', chars))
    print(semcaracter)
else:
    print(cpf)