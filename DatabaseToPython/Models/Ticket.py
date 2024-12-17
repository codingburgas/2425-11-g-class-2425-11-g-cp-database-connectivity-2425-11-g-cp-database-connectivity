import datetime
from Models.Customer import Customer
from Models.Plane import Plane


class Ticket:
    __id = int
    __fromm = str
    __to = str
    __departure_time = datetime
    __arrival_time = datetime
    __seat_number = str
    __plane_id = Plane
    __customer_id = Customer

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def fromm(self):
        return self.__fromm
    @fromm.setter
    def fromm(self, value):
        self.__fromm = value

    @property
    def to(self):
        return self.__to
    @to.setter
    def to(self, value):
        self.__to = value

    @property
    def departure_time(self):
        return self.__departure_time
    @departure_time.setter
    def departure_time(self, value):
        self.__departure_time = value

    @property
    def arrival_time(self):
        return self.__arrival_time
    @arrival_time.setter
    def arrival_time(self, value):
        self.__arrival_time = value

    @property
    def seat_number(self):
        return self.__seat_number
    @seat_number.setter
    def seat_number(self, value):
        self.__seat_number = value

    @property
    def plane_id(self):
        return self.__plane_id
    @plane_id.setter
    def plane_id(self, value):
        self.__plane_id= value

    @property
    def customer_id(self):
        return self.__customer_id
    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id= value