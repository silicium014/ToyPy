import math
class PremierLigue:
    table = ("Manchester City", "Arsenal", "Liverpool", "Manchester United", "Chelsea")
    def stat(self):
        print(*(enumerate(self.__class__.table)), "---------\n")
        print(dir(self), len(dir(self)))
        
    @classmethod
    def info(cls):
        print("Premier ligue", "-----------\n")
        print(dir(cls), len(dir(cls)))
        
        
    @staticmethod
    def matchday():
        help(math)
 
pl = PremierLigue()
pl.stat()
pl.info()
PremierLigue.matchday()