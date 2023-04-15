dia, mes, ano  = input().split()
dia_val, mes_val, ano_val  = input().split()

dia = int(dia)
mes = int(mes)
ano = int(ano)
dia_val = int(dia_val)
mes_val = int(mes_val)
ano_val = int(ano_val)

if ano_val > ano:
    print("na validade")
elif ano_val == ano and not dia > dia_val and mes < mes_val:
    print("vence este ano")
elif ano_val == ano and mes == mes_val and not dia > dia_val:
    print("vence este mês")
else:
    print("vencido!")