# Human - Entity class

class Doctor(Human):
    def __init__(self, name='no name', age=0, alive=True, experience=1):
        self.__name = name
        self.__age = age
        self.__alive = alive
        self.__experience = experience

    def can_cure(self):
        print(self._name + "can cure.")

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, experience):
        if isinstance(experience, int) and experience > 0:
            self.__experience = experience
