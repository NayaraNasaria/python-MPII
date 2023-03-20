from math import sqrt

xa, ya = [int(i) for i in input().split()]
xb, yb = [int(i) for i in input().split()]

distancia = sqrt((xb - xa)**2 + (yb-ya)**2)

print("%.1f" % distancia)
