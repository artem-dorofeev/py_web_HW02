from datetime import datetime

# from Infinity.name import Name
# from Infinity.phone import Phone
# from Infinity.birthday import Birthday
# from Infinity.email_class import Email
# from Infinity.address_class import Address

from name import Name
from phone import Phone
from birthday import Birthday
from email_class import Email
from address_class import Address


class Record:
    def __init__(self, name: Name, birthday: Birthday = None, phone: Phone = None, email: Email = None, user_address: Address = None):
        self.name = name
        self.birthday = birthday
        self.phones = []
        self.emails = []
        self.user_address = user_address

        if phone:
            self.phones.append(phone)

        if email:
            self.emails.append(email)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def delete_phone(self, phone: Phone):
        self.phones = [p for p in self.phones if p.value != phone.value]

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        for phone in self.phones:
            if phone.value == old_phone.value:
                phone.value = new_phone.value
                break

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def check_cont_birthday(self, days):
        if self.birthday:
            birth = self.birthday.value
            current_date = datetime.now()
            next_birth = datetime(current_date.year, birth.month, birth.day)
            if next_birth < current_date:
                next_birth = datetime(current_date.year + 1,
                                      birth.month, birth.day)
            day_for_birth = next_birth - current_date
            if (int(day_for_birth.days)+1) < days:
                day = int(day_for_birth.days) + 1
                age = next_birth.year - birth.year
                return day, age
        return None

    def add_email(self, email: Email):
        self.emails.append(email)

    def change_email(self, old_email: Email, new_email: Email):
        for email in self.emails:
            if email.value == old_email.value:
                email.value = new_email.value

    def delete_email(self, email: Email):
        self.emails = [e for e in self.emails if e.value != email.value]

    def add_address(self, user_address: Address):
        if self.user_address:
            old_user_address = self.user_address
            self.user_address = user_address
            return f'Address of contact "{self.name}" was changed from "{old_user_address}" to "{user_address}"'
        self.user_address = user_address
        return f'Address "{user_address}" was add to contact "{self.name}"'

    def delete_address(self):
        if self.user_address:
            address = self.user_address
            self.user_address = None
            return f'Address "{address}" for contact "{self.name}" was deleted'
        return f'Contact "{self.name}" has no address to delete'

    def __str__(self):
        output = ""
        phones = [phone.value for phone in self.phones]
        phones = ", ".join(phones) if phones else "N/A"
        emails = [email.value for email in self.emails]
        emails = ", ".join(emails) if emails else "N/A"
        birthday = self.birthday.value.date() if self.birthday else "N/A"
        address = self.user_address
        output += f"{self.name.value}: Phones: {phones}, E-mails: {emails}, Birthday: {str(birthday)}, Address: {address}"
        return output
