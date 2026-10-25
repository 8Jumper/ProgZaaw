def checkParzysta(x: int):
    if x % 2 == 0:
        check = True
    else:
        check = False
    if check is True:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")


checkParzysta(67)
