
from collections import UserDict


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Error: no contact."
        except IndexError:
            return "Error: no contact."
    return inner

class Field():
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
    
    def __str__(self):
        return f"Phone: {self.value}"
    
    def validate(self):
        if len(self.value) != 10 or not self.value.isdigit():
            raise ValueError("Phone number must contain exactly 10 digits.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        phone.validate()
        self.phones.append(phone)

    @input_error
    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return
        raise ValueError()

    @input_error
    def edit_phone(self, old_phone_number, new_phone_number):
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number
                phone.validate()
                return
        raise ValueError()

    @input_error
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        raise ValueError()

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    @input_error
    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError()

    @input_error
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError()
