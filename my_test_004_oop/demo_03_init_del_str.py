# demo calss


class Dog:

    def __init__(self, name, color, howl_word):
        self.name = name
        self.color = color
        self.howl_word = howl_word

    def bark(self, ):
        print('%s howl: %s' % (self.name, self.howl_word))
        pass

    def __del__(self):
        print('del dog obj succeed!')
        pass

    def __str__(self):
        return 'the dog\'s info is:\n\tname: %s, color: %s, howl_word: %s' % (self.name, self.color, self.howl_word)


little_black = Dog('little-black', 'black', 'wooooooooo')
little_black.bark()
print(little_black)

del little_black
