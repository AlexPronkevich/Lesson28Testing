from human import Human


# Human - Entity class

class President(Human):
    def __init__(self, name='no name', age=0, alive=True, power=10):
        super().__init__(name, age, alive)
        self.__power = power

    def can_run(self):
        print(self.name + "can run.")

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        if isinstance(power, int) and 0 < power <= 100:
            self.__power = power

    def __str__(self):
        return (super().__str__()
                + f"Power: {self.__power}")
