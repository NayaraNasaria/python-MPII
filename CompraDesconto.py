valor = float(input())
desconto = float(input())

valorComDesconto = valor - (valor * (desconto/100.00))
descontado = valor * (desconto/100.00)

print("%.2f" % valor)
print("%.2f" % valorComDesconto)
print("%.2f" % descontado)


