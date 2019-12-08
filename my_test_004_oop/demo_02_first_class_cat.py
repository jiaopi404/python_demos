# class cat demo
# %x hex


class MyCat:

    def action_eat(self, *args):
        # args => food
        print('cat eat: %s' % args)

    def action_run(self, speed):
        print('cat can run at the speed of: %s' % speed)

    def get_name(self):
        temp = self.name if self.name else 'no name'
        print('the name is: %s' % temp)

    def run_other_func(self):
        print('this func runs other func')
        self.get_name()


jiao_pi = MyCat()

jiao_pi.action_eat(['fish', 'rice'])
jiao_pi.action_run(50)

jiao_pi.name = 'JiaoPi'

print('the location of jiao_pi is: %x' % id(jiao_pi))

jiao_pi.get_name()
jiao_pi.run_other_func()
