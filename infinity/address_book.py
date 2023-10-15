from collections import UserDict
import pickle

#from Infinity.record import Record
from record import Record


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record
        self.save_data()
        return f"\nContact <<< {record} >>> added successfully!"

    def delete_record(self, record: Record):
        del self.data[record.name.value]
        self.save_data()
        return f"\nContact <<< {record.name} >>> removed successfully!"

    def load_data(self):
        try:
            with open('address_book.bin', "rb") as file:
                self.data = pickle.load(file)

        except FileNotFoundError:
            print('\nAddress book is empty!')

    def save_data(self):
        with open('address_book.bin', "wb") as file:
            pickle.dump(self.data, file)

    def search_sample(self, sample: str):
        found_records_list = []
        for name, rec in self.data.items():

            if rec.phones != None and rec.phones != []:
                phones = ' '.join(str(p) for p in rec.phones)
            else:
                phones = 'N/A'

            if rec.birthday != None:
                birthday = str(rec.birthday.value.date())
            else:
                birthday = 'N/A'

            if rec.emails != None and rec.emails != []:
                emails = ' '.join(str(p) for p in rec.emails)
            else:
                emails = 'N/A'

            if rec.user_address != None:
                user_address = str(rec.user_address)
            else:
                user_address = "N/A"

            user_data_str = f"{name} {phones} {emails} {birthday} {user_address}"

            if sample.lower() in user_data_str.lower():
                user_data_dict = {}
                user_data_dict["name"] = name
                user_data_dict["phones"] = phones
                user_data_dict["birthday"] = birthday
                user_data_dict["emails"] = emails
                user_data_dict["address"] = user_address
                found_records_list.append(user_data_dict)
            else:
                continue
        return found_records_list

    def iterator(self, n):

        count = 0
        data_list = []
        for name, record in self.data.items():
            user_data = []
            user_name = name
            if record.birthday != None:
                user_birthday = record.birthday.value.date()
            else:
                user_birthday = 'N/A'

            if record.user_address != None:
                user_address = record.user_address.value
            else:
                user_address = 'N/A'

            user_phones_list = []
            user_phones = record.phones
            user_emails_list = []
            user_emails = record.emails

            if record.phones == None or record.phones == []:
                phones_str = 'N/A'
            else:
                for phone in user_phones:
                    user_phones_list.append(phone.value)
                phones_str = ', '.join(user_phones_list).strip()

            if record.emails == None or record.emails == []:
                emails_str = 'N/A'
            else:
                for email in user_emails:
                    user_emails_list.append(email.value)
                emails_str = ', '.join(user_emails_list).strip()

            user_data = [user_name, phones_str,
                         emails_str, user_birthday, user_address]
            data_list.append(user_data)
            count += 1
            if count >= n:

                yield data_list
                count = 0
                data_list = []

        if data_list:
            yield data_list

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())


if __name__ == "__main__":
    print(UserDict.__dict__)
    c = UserDict
    print(c.__doc__)
    
