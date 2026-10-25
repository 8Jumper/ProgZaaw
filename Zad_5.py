def zad5(x: list, y: int) -> bool:
    for i in x:
        if i == y:
            return True
    return False


lista = [1,2,3,4]
igrek = 4

print(zad5(lista, igrek))
