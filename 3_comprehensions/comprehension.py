a = list(range(10))

print(a)

c = []
for i in a:
    c.append(i*i)
print(c)

b = {x: x*x*x for x in a}

print(b)
print(id(a))
print(id(b))
