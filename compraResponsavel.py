saldo = int(input())
total_carrinho = int(input())

saldo_restante = saldo - total_carrinho

if total_carrinho > saldo:
    print("seu saldo é insuficiente para essa compra")
else:
    print("se você comprar tudo o saldo será:", saldo_restante)
