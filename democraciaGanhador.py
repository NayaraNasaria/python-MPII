num = int(input())
x = 0
y = 0
b = 0
n = 0

for i in range(0, num):
    voto = input()

    if voto == "Y":
        y = y + 1
    elif voto == "X":
        x = x + 1
    elif voto == "B":
        b = b + 1
    elif voto == "N":
        n = n + 1

ben = b + n

print("X", x)
print("Y", y)
print("Brancos e nulos", ben)
if y > x:
    print("vitoria: Y")
elif x > y:
    print("vitoria: X")
else:
    print("empate!")