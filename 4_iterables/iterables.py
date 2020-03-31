import pprint
# list comprehension
# a = range(10)
#
# print(list(a))
#
# print([i*i for i in a])
#
# new_a = list()
# for i in a:
#     new_a.append(i*i)
# print(new_a)
#
# # dict comprehension
#
# new_a3 = dict()
# for i in a:
#     new_a3[i] = i*i*i
# pprint.pprint(new_a3)
#
# words = 'Hello I live in Vinnytsia. It is a very beatiful city city'.split(' ')
# print(words)
#
# comp_words = {len(i) for i in words}
# pprint.pprint(comp_words)



countries_capitals = {
    "Ukraine": "Kyiv",
    "Poland": "Warsaw",
    "United States": "Washington"
}
pprint.pprint(countries_capitals)

capitals_countries = {v: k for k, v in countries_capitals.items()}

pprint.pprint(capitals_countries)

a, *_, c = (1, 2, 3, 4, 5, 6, 6, 7)
print(a)
print(c)
print(c)
print(c)
print(c)
print(c)
print(c)
print(c)
print(c)
print(c)
print(c)
print(c)
print(c)
