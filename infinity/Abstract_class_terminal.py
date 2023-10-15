"""Ваш попередній додаток зараз працює в консольному режимі та взаємодіє з користувачем у вигляді команд в консолі. Додаток треба розвивати і найчастіше змінюваною частиною додатку зазвичай є інтерфейс користувача (поки що це консоль). Модифікуйте код вашого додатку, щоб подання інформації користувачу (виведення карток з контактами користувача, нотатками, сторінка з інформацією про доступні команди) було легко змінити. Для цього треба описати абстрактний базовий клас для користувальницьких уявлень та конкретні реалізації, які успадковують базовий клас та реалізують консольний інтерфейс."""

from abc import ABC


class ConsoleOutputAbstract(ABC):
    def output(self, text: str, *args) -> str:
        ...

class TerminalOutput(ConsoleOutputAbstract):
    def output(self, *args) -> None:
        return args[0]
			
class Commands_Handler:
    def __init__(self, command_output: ConsoleOutputAbstract):
        self.__output_processor = command_output
        
    def print_result(self, *args) -> None:
        return self.__output_processor.output(*args)

if __name__ == "__main__":
    def print_text(text):
        print (text)

    terminal_out = TerminalOutput()

    terminal_handler = Commands_Handler(terminal_out)
      
    #terminal_handler.print_result("New created terminal!", result)\
    terminal_handler.print_result(print_text("hello"), "New created terminal!")
  