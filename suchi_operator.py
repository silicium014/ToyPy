a = [x for x in range(10)]
print('a: {0}'.format(a))
print(f"b :{a[::2]}")
print("id of a = {0}".format(id(a)))
a[0:5] = [44,55,65]
print(a)
print("id of a = {0}".format(id(a)))
# every 2d element
print(a[::2])
# reverse 
print(a[::-1])
# delete all elements with saving list object itself
del a[:]
print(a)
# replace all elements
a[:] = [1,2,3,4,5]
print(a)
# not deep copy
b = a[:]
print(b)