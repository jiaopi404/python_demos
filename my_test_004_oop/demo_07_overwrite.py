# demo overwrite


class Animal:

    def __init__(self):
        print('initial')
        pass

    def snore(self):
        print('snoring')
        pass


class Dog(Animal):
    def __init__(self):
        print('dog initial')
        pass

    def snore(self):
        super().snore()
        print('and snoring')
        pass


little_black = Dog()
little_black.snore()


