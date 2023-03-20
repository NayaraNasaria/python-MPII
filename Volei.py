from collections import defaultdict

time1 = input()
time2 = input()
valores = input()

elementos = defaultdict(int)

for val in valores:
    elementos[val] += 1

if valores == "0":
    print("Início do set")
    print(time1, "0")
    print(time2, "0")
else:
    print(time1, elementos['1'])
    print(time2, elementos['2'])



