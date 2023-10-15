#from Infinity.exceptions import Name_Error
from exceptions import Name_Error

class Name:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):

        if value == None or len(value) == 0:
            raise Name_Error(f"Name cannot be empty")
        if len(value) < 2:
            raise Name_Error(f"Name must have at least 2 symbols: {value}")
        self.__value = value

if __name__ == "__main__":

    #value = ''
    #value = None
    value = "r"
    name  = Name(value)
    print (name)