def print_vector(x, y, z):
    print("<{0}, {1}, {2}>".format(x,y,z))

# usual arguments example    
print_vector(22, 12, 0)

# example without unpacking
tuple_vec = [22, 12, 0]
print_vector(
    tuple_vec[0],
    tuple_vec[1],
    tuple_vec[2]
)

# unpackage from tuple example 
print_vector(*tuple_vec)

# unpackage from dict example 
dict_vec = {'x': 22, 'y': 12, 'z': 0}
print_vector(**dict_vec)
