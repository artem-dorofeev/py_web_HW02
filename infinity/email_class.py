import re

#from Infinity.exceptions import EmailException
from exceptions import EmailException

class Email:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if re.match(r"([A-Za-z]{1}[A-Za-z0-9._]{1,}@[A-Za-z]+\.[A-Za-z]+\.[A-Za-z]{2,})|([A-Za-z]{1}[A-Za-z0-9._]{1,}@[A-Za-z]+\.[A-Za-z]{2,})", value):
            self._value = value
        else:
            raise EmailException(f"Emaile is not correct : {value}")

    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return str(self)
