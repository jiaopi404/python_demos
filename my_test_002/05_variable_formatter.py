# test variable formatter
# %s, %d, %f, %%

print("hello %s" % "world")

print("the price of apple is %6d$" % 20)
print("the price of apple is %06d$" % 20)

print("the price of apple is %.3f$" % 20)

print("the price of apple is %.3f%%" % 20)
