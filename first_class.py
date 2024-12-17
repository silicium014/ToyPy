class SubEx(BufferError):
    def __init__(self):
        super().__init__()
    def static_fn(): # Ведет себя как статическая функция
        print("Ну здорова коль не шутишь !")
    def fn(self):
        print()
        
        
ex = SubEx()
SubEx.static_fn()
print("Size of derived exception class is: {}".format(ex.__sizeof__()))


