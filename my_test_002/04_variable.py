# test variable

a = 20

# type of var
# str type(var)
type_of_a = type(a)
print(type_of_a)

# input
input_value = input("please input something: ")
print(input_value)

# type cast
price = input("please input the price of apple: ")
try:
    price = float(price)
    print("the price is: ")
    print(price)
except ValueError as e:
    # could not convert string to float
    print(e)
