cpf = input()
chars = '.-'

if cpf.__contains__(".") or cpf.__contains__("-"):
    semcaracter = cpf.translate(str.maketrans('', '', chars))
    if len(semcaracter) == 11:
        if semcaracter.isnumeric():
            print(semcaracter)
        else:
            print("ENCODING ERROR")
    else:
        if semcaracter.isnumeric():
            print("SIZE ERROR")
        else:
            print("ENCODING ERROR")
            print("SIZE ERROR")
else:
    print(cpf)