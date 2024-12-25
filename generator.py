def RepeaterGenerator(value, max_count):
    for _ in range(max_count):
        yield value
       
gen = RepeaterGenerator("Hello world!!!", 2)   
for _ in gen:
    try:
        print(_)
    except StopIteration:
        break
        
gen2 = ("Hell'o world again" for _ in range(10) if _%2 == 0)
for x in gen2:
    print(x)

for a in ("Hi Mike Tyson!" for b in range(5)):
    print(a)
    
# variant of generator !!! warning it is can be used once

some_gen = (i**2 for i in range(20))
print(list(some_gen))