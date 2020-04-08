assert 2+2 == 4


def power(x, p):
    assert p > 0
    result = x
    for i in range(p-1):
        result = result * x
    assert result > 0
    return result


print(power(2, 2))


# print(power(2, -2))

print(power(-3, 3))

