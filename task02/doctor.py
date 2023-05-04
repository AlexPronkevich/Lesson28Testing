# Human - Entity class

class Doctor:
    def __init__(self, name='no name', age=0, alive=True, experience=1):
        self.__name = name
        self.__age = age
        self.__alive = alive
        self.__experience = experience

    @property
    def experience(self):
        return self.__experience

    def experience(self, experience):



    @property
    def name(self):
        return self.__name.capitalize()

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age=1):
        if 0 < age <= 120:
            self.__age = age

    @property
    def is_alive(self):
        return "Yes" if self.__alive else "No"

    @is_alive.setter
    def is_alive(self, alive):
        if isinstance(alive, bool):
            self.__alive = alive

    def __str__(self):
        return f"{self.name}: age = {self.__age}. " \
               f"Is alive? - {self.is_alive}"
