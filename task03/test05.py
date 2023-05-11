
class Super:
    def walk(self):
        print("I can walk")

class Subclass(Super):
    pass

base = Super()
sub = Subclass()

print(f"Is base Super? - {isinstance(base, Super)}")   # False
print(f"Is base Subclass? - {isinstance(base, Subclass)}")   # False
print(f"Is sub Super? - {isinstance(sub, Super)}")        # True
print(f"Is sub Subclass? - {isinstance(sub, Subclass)}")    # True

print(f"Is Subclass Super? - {issubclass(Subclass, Super)}")      # True
print(f"Is Super Subclass ? - {issubclass(Super, Subclass)}")      # False
print(f"Is Super object ? - {issubclass(Super, object)}")       # True
print(f"Is Subclass object ? - {issubclass(Subclass, object)}")      # True

