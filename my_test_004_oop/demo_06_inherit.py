# demo inherit

class Animal:

    def __init__(self):
        pass

    def __str__(self):
        return 'Animal'

    def eat(self):
        print('eat')


class Dog(Animal):

    def __init__(self):
        pass

    def bark(self):
        print('bark')


little_black = Dog()
little_black.eat()
little_black.bark()
