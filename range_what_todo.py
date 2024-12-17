import sys
rng = range(0,100**2)
print(dir(rng.__class__))
print(*rng)
print(rng.__sizeof__())
print(sys.getsizeof(range))