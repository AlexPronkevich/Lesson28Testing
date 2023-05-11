class Super(object):
    def __init__(self, id=0):
        self.id = id


class Subclass(Super):
    def __init__(self, id=0, name="no name"):
        super().__init__(id)
        self.name = name

        s = Subclass(1, "Alex")


