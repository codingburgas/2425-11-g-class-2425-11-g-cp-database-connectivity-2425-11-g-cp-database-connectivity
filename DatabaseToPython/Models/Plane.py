class Plane:
    __id = int
    __name = str
    __make = str
    __model = str

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def make(self):
        return self.__make
    @make.setter
    def make(self, make):
        self.__make = make

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model = model