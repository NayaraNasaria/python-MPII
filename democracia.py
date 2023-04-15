candidata1 = int(input())
candidata2 = int(input())
candidata3 = int(input())
candidata4 = int(input())

if candidata1 > candidata2 and candidata1 > candidata3 and candidata1 > candidata4:
    print("maior:", candidata1)
elif candidata2 > candidata1 and candidata2 > candidata3 and candidata2 > candidata4:
    print("maior:", candidata2)
elif candidata3 > candidata1 and candidata3 > candidata2 and candidata3 > candidata4:
    print("maior:", candidata3)
elif candidata4 > candidata3 and candidata4 > candidata2 and candidata4 > candidata1:
    print("maior:", candidata4)