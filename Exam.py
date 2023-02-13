#Problem2
import datetime

class Product:
    def __init__(self, price:int, id:int, quantity:int):
        self.price = price
        self.id = id
        self.quantity = quantity
    def __repr__(self):
        return "{} {} {}".format(self.price, self.id, self.quantity)
    # @property
    # def price(self):
    #     return self.__price
    # @price.setter
    # def set_price(self, value):
    #     self.__price = value
    # @property
    # def id(self):
    #     return self.__id
    # @id.setter
    # def set_id(self, id):
    #     self.__id = id
    # @property
    # def quantity(self):
    #     return self.__quantity
    # @quantity.setter
    # def set_quantity(self, quantity):
    #     self.__quantity = quantity

    def buy(self, count):
        if(count>self.__quantity):
            raise Exception("The count is greater than quantity")
        else:
            self.quantity = count


class Inventory:
    def __init__(self):
        self.products = []
    def __repr__(self):
        return "{}".format(self.products)

    def get_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product

    def sum_of_products(self):
        sum = 0
        for product in self.products:
            sum += product.price * product.quantity
        return sum

inventory = Inventory()
product1 = Product(120000, 1234567, 78)
product2= Product(6789, 23456789, 80)
print(product2)
print(product1)
print(inventory.get_by_id(product1))
print(inventory.get_by_id(product2))
sum = inventory.sum_of_products()
print("Sum of all products", sum)

#Problem1
class Patient:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        if(age>=18 or age<=100):
            raise Exception("Can't be accepted")
        else:
            self.age = age
        self.gender = gender
    def __repr__(self):
        return "{} {} - {}, {} years old".format(self.name, self.surname, self.age, self.gender)

    def __ne__(self, other):
        if isinstance(other, Patient):
            return self.name != other.name or self.surname != other.surname or self.age!=other.age or self.gender!=other.gender
class Doctor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.schedule = {}
    def __repr__(self):
        schedule = "\n".join([f"{datetime}: {patient}" for datetime, patient in self.schedule.items()])
        return f"Doctor(name={self.name!r}, surname={self.surname!r}, schedule=\n{schedule})"
    def register_patient(self, patient, datetime):
        if self.is_registered(patient):
            return f"Patient {patient}already registered at {datetime}."
        elif not self.is_free(datetime):
            return f"Datetime {datetime}is taken."
        else:
            self.schedule[datetime] = patient
            next_slot = datetime + 30
            self.schedule[next_slot] = "Not Available"
            return f"Patient{patient} added successfully at {datetime}."

    def is_free(self, datetime):
        for i in range(2):
            if datetime + 30 * i in self.schedule.keys():#there is error in this line but I can't solve it
                return False
        return True

    def is_registered(self, patient):
        for p in self.schedule.values():
            if p == patient:
                return True
        return False

doc1 = Doctor("John", "Smith", )
patient1 = Patient("Bob", "lalala", 13, "M")
patient2 = Patient("Anna", "darwin", 45, "F")
patient3 = Patient("Ashot", "proshyan", 78, "M")
print(doc1.register_patient(patient1, datetime.datetime(2023, 5, 14, 9, 0)))
print(doc1.register_patient(patient2, datetime.datetime(2023, 2, 14, 9, 0)))
print(doc1.register_patient(patient3, datetime.datetime(2023, 2, 14, 9, 0)))

print(doc1.is_registered(patient2))
print(doc1.is_registered(patient3))

print(patient1!=patient2)

#Problem3
class Passenger:# doc1 = Doctor("John", "Smith", )
# patient1 = Patient("Bob", "lalala", 13, "M")
# patient2 = Patient("Anna", "darwin", 45, "F")
# patient3 = Patient("Ashot", "proshyan", 78, "M")
# print(doc1.register_patient(patient1, datetime.datetime(2023, 5, 14, 9, 0)))
# print(doc1.register_patient(patient2, datetime.datetime(2023, 2, 14, 9, 0)))
# print(doc1.register_patient(patient3, datetime.datetime(2023, 2, 14, 9, 0)))
#
# print(doc1.is_registered(patient2))
# print(doc1.is_registered(patient3))
#
# print(patient1!=patient2)

    def __init__(self, name, city:str):
        self.__name = name
        self.__city = city
        self.__rooms = {}
    @property
    def name(self):
        return self.__name
    @property
    def city(self):
        return self.city
    @property
    def rooms(self):
        return self.rooms
    def __repr__(self):
        return "{} {} {}".format(self.__name, self.__city, self.__rooms)

    # def add_room(self, room_number, room_type, count):
    #     self.rooms[room_number] = {'type': room_type, 'count': count}
class Hotel:
    def __init__(self, city:str,):
        self.__city = city
        self.rooms = {}
    def __repr__(self):
        return "{} {}".format(self.city, self.rooms)
    @property
    def get_city(self):
        return self.__city

    def free_rooms_list(self, room_type):
        return self.rooms[room_type]
    def reserve_rooms(self, room_type):
        if room_type not in self.rooms:
            raise Exception(f'Room type {room_type} does not exist.')
        if self.rooms[room_type] == 0:
            raise Exception(f'No rooms of type {room_type} are available.')

        self.rooms[room_type]-= 1

hotel = Hotel('New York')
passenger1 = Passenger("Hayk", "New York")
# passenger1.add_room(123, 'single', 300)
# passenger1.add_room(143, 'double', 400)
# passenger1.add_room(1568, 'penthouse', 40)
print(passenger1.city)
print(passenger1.rooms)
print(hotel.free_rooms_list("single"))
print(hotel.reserve_rooms("single"))
print(hotel.reserve_rooms("single"))