def printNums(num):
    for val in range(num):
        yield val

def chainingFunc(generator):
    for val in generator:
        yield val**2

print(list(chainingFunc(printNums(20))))

    