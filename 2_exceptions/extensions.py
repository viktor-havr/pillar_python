a = '1'
try:
    a[2]
    a = int('text')
    raise None
finally:
    print('I`m not Misha anymore!')
print(a)
print('Hello, I`m after the error!')
