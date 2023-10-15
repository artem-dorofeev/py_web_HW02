import re
import os
from rich.table import Table
from rich.console import Console

# from Infinity.record import Record
# from Infinity.email_class import Email
# from Infinity.address_class import Address
# from Infinity.name import Name, Name_Error
# from Infinity.phone import Phone
# from Infinity.birthday import Birthday
# from Infinity.address_book import AddressBook
# from Infinity.exceptions import PhoneMustBeNumber, BirthdayException, EmailException, Name_Error
# from Infinity.sort_folder import sort
# from Infinity.suggest import suggest_command
# from Infinity.note import note_book
# from Infinity.Abstract_class_terminal import ConsoleOutputAbstract, Commands_Handler, TerminalOutput

from record import Record
from email_class import Email
from address_class import Address
from name import Name, Name_Error
from phone import Phone
from birthday import Birthday
from address_book import AddressBook
from exceptions import PhoneMustBeNumber, BirthdayException, EmailException, Name_Error, NoComandError
from sort_folder import sort
#from suggest import suggest_command
from note import note_book
from Abstract_class_terminal import ConsoleOutputAbstract, Commands_Handler, TerminalOutput

console = Console()

terminal_out = TerminalOutput()
terminal_handler = Commands_Handler(terminal_out)

I = 1

address_book = AddressBook()


def sort_folder_command(args):
    return sort()


def address_book_commands():
    table_address_book = Table(
        title="\nALL COMMANDS FOR ADDRESS BOOK:\nImportant!!! All entered data must be devided by gap! Phone number must have 10 or 12 digits!\n * - optional paramiters")
    table_address_book.add_column("COMMAND", justify="left")
    table_address_book.add_column("NAME", justify="left")
    table_address_book.add_column("PHONE NUMBER", justify="left")
    table_address_book.add_column("EMAIL", justify="left")
    table_address_book.add_column("BIRTHDAY", justify="left")
    table_address_book.add_column("ADDRESS", justify="left")
    table_address_book.add_column("DESCRIPTION", justify="left")
    table_address_book.add_row(
        "hello / hi", "-", "-", "-", "-", "-", "Greeting")
    table_address_book.add_row("add record", "Any name", "Phone number *",
                               "Email *", "YYYY-MM-DD *", ": + Address *", "Add new contact")
    table_address_book.add_row(
        "delete record", "Name to delete", "-", "-", "-", "-", "Delete contact")
    table_address_book.add_row("add address / change address",
                               "Existing name", "-", "-", "-", ": + Address", "Add address")
    table_address_book.add_row("delete address / remove address", "Existing name",
                               "-", "-", "-", ": + Address to delete", "Delete address")
    table_address_book.add_row("add phone", "Existing name",
                               "Additional phone number", "-", "-", "-", "Add phone number")
    table_address_book.add_row("change phone", "Existing name",
                               "Old phone number + new phone number", "-", "-", "-", "Change phone number")
    table_address_book.add_row("delete phone", 'Existing name',
                               'Phone nunber to delete *', "-", "-", "-", "Delete phone number")
    table_address_book.add_row(
        "add birthday", 'Existing name', "-", "-", "YYYY-MM-DD", "-", "Add birthday")
    table_address_book.add_row("days to birthday / dtb", "-", "-",
                               "-", "-", "-", "Show contact's birthday in chosen period")
    table_address_book.add_row(
        "add email", 'Existing name', "-", "Email", "-", "-", "Add email")
    table_address_book.add_row("change email", 'Existing name',
                               "-", "Old email + new email", "-", "-", "Change email")
    table_address_book.add_row(
        "delete email", 'Existing name', "-", "Email to delete", "-", "-", "Delete email")
    table_address_book.add_row(
        "show all", "-", "-", "-", "-", "-", "Getting Address Book (by default)")
    table_address_book.add_row("show all + N", "-", "-", "-",
                               "-", "-", "Getting Address Book by N records on the page")
    table_address_book.add_row("search + sample", "-", "-", "-",
                               "-", "-", 'searching <<< sumple >>> in address book')
    table_address_book.add_row(
        "sort", "-", "-", "-", "-", "-", "Sorting folder in the enetered path")
    table_address_book.add_row(
        "note", "-", "-", "-", "-", "-", "Opens Note Book. Use \"help\" inside Note Book to see all commands ")
    table_address_book.add_row(
        "good bye / close / exit", "-", "-", "-", "-", "-", "Exit")
    table_address_book.add_row(
        "help", "-", "-", "-", "-", "-", "Printing table of commands")
    
    return console.print(table_address_book)


def note_command(args):
    return note_book()


def exit_command(args):
    address_book.save_data()
    return '\nGood bye! Have a nice day!\n'


def help_command(args):
    return address_book_commands()


def show_all_command(args):

    if len(address_book.data) == 0:
        return '\nAddress Book is empty!'

    n = 10
    k = 1

    if len(args[1]) > 0:

        try:
            n = int(args[1][0])
        except ValueError:
            print(
                f'\nEnterd number <<< {args[0]} >>> of pages does not represent a valid integer!\nDefault number of records N = {n} is used')

    for block in address_book.iterator(n):

        table = Table(title=f"\nADDRESS BOOK page {k}")
        table.add_column("Name", justify="left")
        table.add_column("Phone number", justify="left")
        table.add_column("Email", justify="left")
        table.add_column("Birthday", justify="left")
        table.add_column("Address", justify="left")
        for item in block:
            table.add_row(str(item[0]), str(item[1]), str(
                item[2]), str(item[3]), str(item[4]))
        
        console.print(table)

        k += 1

        if len(block) == n:
            input("\nTo see next page press any key:\n>>>")

    return "End of address book."


def search_command(args):

    sample_name = args[0]
    if args[1] != []:
        sample_data = args[1][0]
    else:
        sample_data = ""

    sample = sample_name + sample_data

    if sample == '':
        return "\nMissing sample for search!"

    found_records_list = address_book.search_sample(sample)

    if len(found_records_list) > 0:

        table = Table(
            title=f"\nALL FOUND RECORDS ACCORDING TO SAMPLE <<< {sample} >>>")
        table.add_column("Name", justify='left')
        table.add_column("Phone number", justify="left")
        table.add_column("Email", justify="left")
        table.add_column("Birthday", justify="left")
        table.add_column("Address", justify="left")

        for item in found_records_list:
            table.add_row(item["name"], item["phones"],
                          item["emails"], item['birthday'], item["address"])
        #return table
        return console.print(table)
    else:
        return f"\nThere is now any record according to sample <<< {sample} >>>"


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Invalid command. Please try again."
        except ValueError:
            return "Error: Invalid input format. Please try again."
        except IndexError:
            return "Error: Contact not found. Please try again."
        except PhoneMustBeNumber as e:
            return f"PhoneMustBeNumber: {e}"
        except BirthdayException as e:
            return f"BirthdayException: {e}"
        except EmailException as e:
            return f"EmailException: {e}"
        except Name_Error as e: 
            return f"Name_error : {e}"
        except NoComandError as e:
            return f'NoComandError : {e}'
        # except TypeError:
        #     return "Format birthday must be YYYY/MM/DD"
    return wrapper


@input_error
def add_record(args: tuple[str]) -> str:
    name = Name(args[0])
    birthday = phone = email = address = None
    for i in args[1]:
        try:
            phone = Phone(i)
            continue
        except Exception:
            pass

        try:
            email = Email(i)
            continue
        except Exception:
            pass

        try:
            birthday = Birthday(i)
            continue
        except Exception:
            pass

    if args[2]:
        address = Address(args[2])

    rec: Record = address_book.get(str(name))
    if rec:
        return f'Record with name {str(name)} is already in address book'
    return address_book.add_record(Record(name, birthday, phone, email, address))


@input_error
def delete_record_command(args):
    try:
        name = args[0]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"

        record = address_book[name]
        address_book.delete_record(record)

        return f"\nContact {name} has been deleted successfully!"

    except:
        raise ValueError


@input_error
def add_phone_command(args):

    if args[0] and len(args[1]) == 1:
        name = args[0]
        record = address_book[name]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        phone = Phone(args[1][0])
        record.add_phone(phone)
        return f"A number {phone.value} has been added to a contact {name}"

    else:
        raise ValueError


@input_error
def change_phone_command(args):

    if args[0] and len(args[1]) == 2:
        name = args[0]
        old_phone, new_phone = args[1]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        o_phone = Phone(old_phone)
        n_phone = Phone(new_phone)
        record = address_book[name]
        record.change_phone(o_phone, n_phone)
        return f"The phone number {old_phone} for contact {name} has been changed to {new_phone}."
    else:
        raise ValueError


@input_error
def add_birthday_command(args):
    if args[0] and len(args[1]) == 1:
        name = args[0]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        birthday = Birthday(args[1][0])
        record = address_book[name]
        if record.birthday:
            return f"Contact with name: {name} already has a date of birth"
        record.add_birthday(birthday)
        return f"Birthday: {birthday} to contact: {name} has been added"
    else:
        raise ValueError


@input_error
def days_to_birthday_command(args):
    day = int(args[1][0])
    list_bd = ''
    for key, value in address_book.items():
        rec = address_book.get(str(key))
        result = rec.check_cont_birthday(day)
        if result:
            list_bd += f'Contact {key}: birthday through {result[0]} days ({result[1]} years old)\n'
    if len(list_bd) < 1:
        list_bd = f'No birthdays in this period'
    return list_bd.strip()


@input_error
def delete_phone_command(args):
    if args[0] and len(args[1]) == 1:
        name = args[0]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        phone = Phone(args[1][0])
        record = address_book[name]
        record.delete_phone(phone)
        return f"For contact {name} phone {phone.value} has been deleted"

    else:
        raise ValueError


@input_error
def add_email_command(args):
    if args[0] and len(args[1]) == 1:
        name = args[0]
        record = address_book[name]
        if name not in address_book.data:
            return f"You dont have contact with name: {name}"
        email = Email(args[1][0])
        record.add_email(email)
        return f"Email: {email} for contact: {name} has been added"
    else:
        raise ValueError


@input_error
def change_email_command(args):
    if args[0] and len(args[1]) == 2:
        name = args[0]
        old_email, new_email = args[1]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        o_email = Email(old_email)
        n_email = Email(new_email)
        record = address_book[name]
        record.change_email(o_email, n_email)
        return f"The email {old_email} for contact {name} has been changed to {new_email}."
    else:
        raise ValueError


@input_error
def delete_email_command(args):
    if args[0] and len(args[1]) == 1:
        name = args[0]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        email = Email(args[1][0])
        record = address_book[name]
        record.delete_email(email)
        return f"For contact {name} email {email.value} has been deleted"

    else:
        raise ValueError


# def no_command(args) -> str:
#     suggest = suggest_command(args[0])
#     if suggest:
#         return f'You made a mistake, maybe you mean "{suggest}"? Try again'
#     return 'Unknown command'


def hello_command(args) -> str:
    return 'How can I help you?'


@input_error
def add_address(args):
    name = Name(args[0])
    rec: Record = address_book.get(str(name))
    if not rec:
        return f'No record with name {name}'
    return rec.add_address(Address(args[2]))


@input_error
def delete_address_command(args):
    name = Name(args[0])
    rec: Record = address_book.get(str(name))
    if not rec:
        return f'No record with name {name}'
    return rec.delete_address()


COMMANDS = {
    add_record: ("add record",),
    add_address: ("add address", "change address"),
    change_phone_command: ("change phone",),
    add_phone_command: ("add phone",),
    exit_command: ("good bye", "close", "exit",),
    help_command: ("help",),
    delete_phone_command: ("delete phone",),
    add_birthday_command: ("add birthday",),
    show_all_command: ("show all",),
    search_command: ("search",),
    hello_command: ("hello", 'hi',),
    add_email_command: ("add email",),
    change_email_command: ("change email",),
    delete_email_command: ("delete email",),
    delete_record_command: ("delete record", "remove",),
    delete_address_command: ("delete address", "remove address",),
    days_to_birthday_command: ("days to birthday", "dtb",),
    sort_folder_command: ("sort",),
    note_command: ("note",)
}


def get_user_name(user_info: str) -> tuple:

    regex_name = r'[a-zA-ZА-Яа-я]+'
    name = ''
    user_address = ''
    address_separator = ':'
    if address_separator in user_info:
        data = user_info.split(address_separator)
        user_info_list = data[0].strip().split()
        user_address = data[1].strip()
    else:
        user_info_list = user_info.strip().split()

    if user_info:
        while user_info_list:
            word = user_info_list[0]
            match_name = re.match(regex_name, word)
            if match_name and len(match_name.group()) == len(word):
                name = name + word.capitalize() + ' '
                user_info_list.remove(word)
            else:
                break

    return name.strip(), user_info_list, user_address

def parser(user_input: str):
    user_info = ''
    user_input_lower = user_input.lower()
    for command, kwds in COMMANDS.items():
        for kwd in kwds:
            if user_input_lower.startswith(kwd):
                user_info = user_input[len(kwd):].strip()
                return command, user_info
    else:
        result = "\nUnknown command! Try again!"
        print (terminal_handler.print_result(result))
        return main()
    

    #return no_command, user_input

def clear_terminal():
    if os.name == 'posix':  # For Unix-like systems (Linux, macOS)
        os.system('clear')
    elif os.name == 'nt':   # For Windows
        os.system('cls')

def main():

    global I
    if I == 1:
        address_book.load_data()
        result = address_book_commands()
        terminal_handler.print_result(result)
        I += 1

    while True:
        user_input = (input(f'\nMAIN: Enter command, please!\n\n>>>')).strip()

        clear_terminal()

        command, user_info = parser(user_input)

        user_data = get_user_name(user_info)

        result = command(user_data)

        print (terminal_handler.print_result(result))

        if command == exit_command:
            break


if __name__ == "__main__":
    main()
