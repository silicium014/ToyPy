encoded_str = "Hello world!".encode("ascii")

print(encoded_str)
print("Тип кодированной строки: {}".format(type(encoded_str)))
print("Original size {}".format(encoded_str.decode().__sizeof__()))
print("Encoded size {}".format(encoded_str.__sizeof__()))
print(*encoded_str.decode())
print(*encoded_str)