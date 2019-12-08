# demo for private variable or function


class Women:

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        pass

    def __str__(self):
        return 'name: %s, age: %s' % (self.name, self.get_age())

    def get_age(self):
        return self.__age


van_jim = Women('wang jing', 24)
print(dir(van_jim))
