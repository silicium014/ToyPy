class RepeaterAlternative:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return self
    def __next__(self):
        return self.value
        

class Repeater:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return RepeaterIterator(self)
        
class RepeaterIterator:
    def __init__(self, source):
        self.source = source
    def __next__(self):
         return self.source.value
'''  
for element in Repeater("Hello world!!!"):
    print(element)
'''# the same as 

repeater = RepeaterAlternative("Hello world!!!")
iterator = repeater.__iter__()
while True:
    item = iterator.__next__()
    print(item)
    
   
    
  