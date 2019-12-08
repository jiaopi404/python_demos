# test func of hash

a = 2

b = 2

c = [1, 2, 3]

d = [1, 2, 3]

e = d

print('hash of a is: %s, hash of b is: %s' % (hash(a), hash(b)))
print('hash of c\'s id is: %s, hash of d\'s id is: %s, hash of e\'s id is: %s' % (hash(id(c)),
                                                                                  hash(id(d)),
                                                                                  hash(id(e))))
