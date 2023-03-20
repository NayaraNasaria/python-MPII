variavel = input()

if variavel.startswith("_") or variavel.isalnum() and variavel[0].isalpha() or variavel.isidentifier():
    print("OK")
else:
    print("ERROR")
