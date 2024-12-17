class BoundedRepeater:
    def __init__(self, value, repeat_count):
        self.value = value
        self.repeat_count = repeat_count
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.repeat_count:
            raise StopIteration
        self.count+=1
        return self.value

repeater = BoundedRepeater("Hello world!!", 20)
iterator = repeater.__iter__()
while True:
        try:
            item = iterator.__next__()
        except StopIteration:
            break
        print(item)
         
        
        