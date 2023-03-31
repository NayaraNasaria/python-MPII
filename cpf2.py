cpf = input()
chars = '.-'

if cpf.__contains__(".") or cpf.__contains__("-"):
    semcaracter = cpf.translate(str.maketrans('', '', chars))
    if len(semcaracter) == 11:
        print(semcaracter)
        print("OK")
    else:
        print(semcaracter)
        print("ERROR")
else:
    print(cpf)