meninas = int(input())
dias = int(input())

monitores = int(input())

demanda = int(input())
dias_demanda = int(input())

meninasDias = meninas*dias
demandaDias = demanda*dias_demanda
monitoresD = demandaDias*monitores
resultado = monitoresD/meninasDias

print(int(resultado))