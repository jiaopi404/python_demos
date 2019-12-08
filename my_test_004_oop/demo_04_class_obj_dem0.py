# demo go shopping
import random


class Person:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.init_money = money
        self.shop_car = []
        print('hello, you have %s$' % self.money)
        pass

    def __str__(self):
        connection_str = ', '
        return '%s has %s$, he buy %s. Finally, he left %s$.' % (self.name, self.init_money, connection_str.join(self.shop_car), self.money)

    def buy(self, good):
        if good.price > self.money:
            print('sorry man, you can\'t afford it! you have %s$ left!' % self.money)
            return False
        else:
            self.money -= good.price
            self.shop_car.append(good.name)
            print('You have %s$ left!' % self.money)
            return True


class Goods:

    def __init__(self, good_name, good_price):
        self.name = good_name
        self.price = good_price
        pass

    def __str__(self):
        return '%s\'s price is: %s' % (self.name, self.price)


goods_list = []

apple = Goods('apple', 2)
phone = Goods('xiaomi', 1200)
cup = Goods('cup', 200)
cloth = Goods('cloth', 300)
shoe = Goods('shoe', 400)
fake_girl_friend = Goods('fake_girl_friend', 8000)

goods_list.append(apple)
goods_list.append(phone)
goods_list.append(cup)
goods_list.append(cloth)
goods_list.append(shoe)
goods_list.append(fake_girl_friend)

# shuffle the list
random.shuffle(goods_list)

# give you money
random_money = random.randint(100, 20000)

jiao_pi = Person('jiao_pi', random_money)

for good in goods_list:
    print(good)
    can_buy = jiao_pi.buy(good)
    if not can_buy:
        break

print(jiao_pi)
