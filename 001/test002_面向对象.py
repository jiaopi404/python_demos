class Person:

	def __init__(self, name, weight):
	
		self.name = name
		self.weight = weight
		
	def __str__(self):
	
		return "my name is %s , weight is %.2f kg" % (self.name, self.weight)
	
	def run(self):
		pass
		
	def eat(self):
		pass

xiaoming = Person("cyk", 75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)