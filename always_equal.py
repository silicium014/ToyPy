class AlwaysEqual:
    def __eq__(self, other):
        return True
    def __has__(self):
        return id(self)

print(AlwaysEqual() == False)