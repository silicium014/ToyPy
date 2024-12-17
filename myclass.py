class SubEx(BufferError):
    def __init__(self):
        super().__init__()
    def static_fn(): # Ведет себя как статическая функция
        print("Ну здорова коль не шутишь, это почти статическая функция!")
    def fn(self):
        print(type(SubEx))
        
        
ex = SubEx()
ex.fn()
SubEx.static_fn()



