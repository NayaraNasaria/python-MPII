algarismos = []
algarismos.append(input())
algarismos.append(input())
algarismos.append(input())
algarismos.append(input())
algarismos.reverse()
convertString = " ".join(algarismos).replace(" ", "")
numero_grandao = int(convertString) + 1

print(numero_grandao)