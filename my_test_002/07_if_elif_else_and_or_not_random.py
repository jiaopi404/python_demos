# test if else

import random

temp = random.randint(1, 100)
print("temp is: %d" % temp)

if temp > 90:
    print("good")
elif temp >= 60 and temp <= 90:
    print("not bad")
else:
    print("bad")
