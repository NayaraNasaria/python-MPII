msg = input()
SOS = "...---..."

if msg.__contains__(SOS):
    print("S")
else:
    print("N")