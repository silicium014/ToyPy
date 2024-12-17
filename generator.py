def RepeaterGenerator(value):
   while True:
        yield value

print(dir(RepeaterGenerator))
gen = RepeaterGenerator("Hello world!!!")  
print(dir(gen))     
for _ in gen:
    print(_)
