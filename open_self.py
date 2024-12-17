fwrite = open("open_self.py", "r")
print(fwrite.__sizeof__())
for str in fwrite:
    print(str)
fwrite.close()
