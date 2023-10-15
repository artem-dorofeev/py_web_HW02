from datetime import datetime, date

#from Infinity.exceptions import BirthdayException
from exceptions import BirthdayException

class Birthday:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            #self._value = datetime.strptime(value, "%Y/%m/%d")
            self._value = datetime.strptime(value, "%Y-%m-%d")
        except:
            raise BirthdayException(f"Format birthday must be in format YYYY-MM-DD: {value}")

    def __str__(self) -> str:
        if self._value:
            return self._value.strftime("%Y-%m-%d")

    def __repr__(self) -> str:
        return str(self)
