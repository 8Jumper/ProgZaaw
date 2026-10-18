longIntList = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

def printSteamy(list):
    for x in range(10):
        if list[x]%2==0:
            print(list[x])

printSteamy(longIntList)