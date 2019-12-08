# demo test variable storage location

a = 2

b = a

a = 3

print(b)  # 2

c = [1, 2, 3]

d = c

c = 5

print(d)  # [1, 2, 3]
print('id of b is %s, id of d is %s' % (id(b), id(d)))

# conclusion: just like javascript, basic types are value-copied, but reference type are pointer-copied
