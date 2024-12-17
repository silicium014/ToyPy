import sys
a = [1,2]
b = (1,2)
c = {'1': 2}
d = 5
e = 5.1444483837
f = "Hello world"
g = True
def h():
    return print(f)
i = None
j = range(100)
class Base:
    pass
k = Base()
l = {1,2,3}
print('Object "a" is type: {} and size: {}'.format(type(a), a.__sizeof__()))
print('Object "b" is type: {} and size: {}'.format(type(b), b.__sizeof__()))
print('Object "c" is type: {} and size: {}'.format(type(c), c.__sizeof__()))
print('Object "d" is type: {} and size: {}'.format(type(d), d.__sizeof__()))
print('Object "e" is type: {} and size: {}'.format(type(e), e.__sizeof__()))
print('Object "f" is type: {} and size: {}'.format(type(f), f.__sizeof__()))
print('Object "g" is type: {} and size: {}'.format(type(g), g.__sizeof__()))
print('Object "i" is type: {} and size: {}'.format(type(i), i.__sizeof__()))
print('Object "j" is type: {} and size: {}'.format(type(j), j.__sizeof__()))
print('Object "Base" is type: {} and size: {}'.format(type(Base), object.__sizeof__(Base)))
print('Object "h" is type: {} and size: {}'.format(type(h), h.__sizeof__()))
print('Object "k" is type: {} and size: {}'.format(type(k), k.__sizeof__()))
print('Object "l" is type: {} and size: {}'.format(type(l), l.__sizeof__()))
print('Object "enumerate" is type: {} and size: {}'.format(type(enumerate), sys.getsizeof(enumerate)))