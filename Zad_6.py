def Zad6(x: list, y: list) -> list:
    for i in x:
        if i not in y:
            y.append(i)
    k = 0
    for i in y:
        q = pow(i,3)
        y[k] = q
        k+=1
    return y


x = [1,1,2,3]
y = [1,4,5]

print(Zad6(x,y))
