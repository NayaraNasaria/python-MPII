ano = int(input())

seculo = (ano / 100) + 1

if ano <= 100:
    print(1)
else:
    print(int(seculo))
