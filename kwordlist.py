print('Program starting....')
def f(*dct, **kwords):
    print("Param *dct : {}".format(type(dct)))
    print("Param **kwords : {}".format(type(kwords)))
    print("This is function: {}".format(type(f)))
    print("Size of function: {0}".format(f.__sizeof__()))
    
f()

if __name__ == "__main__":# Значит мы запускаемся как скрипт, а не подключены как модуль
    print("I am in main: {}!".format(__name__))
    print(dir("Hi"))
    
