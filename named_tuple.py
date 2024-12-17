from collections import namedtuple

Car = namedtuple('auto', 'color km_gone automatic')

mazda = Car('red', 150, True)
print(mazda)
print(mazda.color)