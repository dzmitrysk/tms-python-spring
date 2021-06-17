class Dog:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


dog = Dog("Charlie")
print(f"Name: {dog.get_name()}")

# print(f"Name: {dog.__name}")