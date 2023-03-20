val1 = int(input())
operador = input()
val2 = int(input())

if operador == "/":
    div = val1/val2
    print("%.1f" % div)
elif operador == "//":
    divInteira = val1//val2
    print(divInteira)
elif operador == "%":
    modulo = val1 % val2
    print(modulo)