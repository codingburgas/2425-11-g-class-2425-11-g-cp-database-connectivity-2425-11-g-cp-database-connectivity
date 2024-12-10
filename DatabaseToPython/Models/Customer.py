class Customer:
    __id = int
    __first_name = str
    __last_name = str
    __country = str
    __age = int

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, value):
        self.__country = value

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value
