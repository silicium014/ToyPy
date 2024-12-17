def RepeaterGenerator(value, max_count):
    for _ in range(max_count):
        yield value
        
#print(dir(RepeaterGenerator))
gen = RepeaterGenerator("Hello world!!!", 2)  
print(dir(gen))    
for _ in gen:
    print(_)
