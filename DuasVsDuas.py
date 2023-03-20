menina1Dupla1 = int(input())
menina1Dupla2 = int(input())
menina2Dupla1 = int(input())
menina2Dupla2 = int(input())

if menina1Dupla1 > menina1Dupla2 and menina1Dupla1 >= menina2Dupla1 and menina1Dupla1 > menina2Dupla2:
    print(menina1Dupla1)

elif menina1Dupla2 > menina1Dupla1 and menina1Dupla2 > menina2Dupla1 and menina1Dupla2 >= menina2Dupla2:
    print(menina1Dupla2)

elif menina2Dupla1 > menina1Dupla1 and menina2Dupla1 > menina1Dupla2 and menina2Dupla1 > menina2Dupla2:
    print(menina2Dupla1)

elif menina2Dupla2 > menina1Dupla1 and menina2Dupla2 > menina1Dupla2 and menina2Dupla2 > menina2Dupla1:
    print(menina2Dupla2)
else:
    print("empate")
