from collections import UserDict
from datetime import datetime
import cmd
import pickle


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
            self.__value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Birthday(Field):
    @Field.value.setter
    def is_valid_birthday(self, value: str):
        try:
            self._value = datetime.strptime(value, '%Y.%m.%d').date()
            return True
        except ValueError:
            return False


class Phone(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Invalid phone number")
        super().__init__(value)

    @Field.value.setter
    def validate(value):
        return isinstance(value, str) and len(value) == 10 and value.isdigit()


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    def find_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj

    def edit_phone(self, old_phone, new_phone):
        phone_found = False
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                new_phone_obj = Phone(new_phone)
                if not phone.value:
                    raise ValueError("Invalid phone number")
                self.phones[i] = new_phone_obj
                phone_found = True
                break
        if not phone_found:
            raise ValueError("Phone number not found in the list")

    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
                break

    def days_to_birthday(birthdate):
        today = datetime.now().date()
        next_birthday = datetime(today.year, birthdate.month, birthdate.day).date()
        if today > next_birthday:
            next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day).date()
        days_until_birthday = (next_birthday - today).days
        return days_until_birthday
    

class AddressBook(UserDict):
    def __init__(self, file="address_book.pickle"):
        super().__init__()
        self.file = file    

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        results = []
        for name, record in self.data.items():
            if name.lower() in name.lower():
                results.append(record)
            else:
                for phone in record.phones:
                    if name in phone.value:
                        results.append(record)
                        break
        return results

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            
    def iterator(self, item_number):
        counter = 0
        result = ''
        for item, record in self.data.items():
            result += f'{item}: {record}'
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = ''

    def dump(self):
        with open(self.file, 'wb') as file:
            pickle.dump(self.data, file)

    def load(self):
        try:
            with open(self.file, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            pass


class Controller(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.book = AddressBook()

    def save(self):
        self.book.dump()

    def loading(self):
        self.book.load()

    def exit(self):
        self.book.dump()
        return True

    def do_search(self, arg):
        results = self.book.find(arg)
        if results:
            for record in results:
                print(record)
        else:
            print("No records found.")

if __name__ == "__main__":
    controller = Controller()
    controller.cmdloop()