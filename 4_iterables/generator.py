

def odd_gen():
    yield 20
    yield 21
    yield 22
    yield 23
    yield 24
    yield 25


g = odd_gen()
g2 = odd_gen()
g3 = odd_gen()
print(g)
print(g2)
print(g3)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for i in g:
    print(i)
