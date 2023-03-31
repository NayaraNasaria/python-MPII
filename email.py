vezes = int(input())
naocontem = 0
caractere_contem = 0

for vezes in range(0, vezes):
    email = input()

    if email.__contains__('@'):
        caractere_contem = caractere_contem + 1
    else:
        naocontem = naocontem + 1

print(naocontem)