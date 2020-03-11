import sys
def to_date():
    print("Введіть кількість секунд")
    s = int(sys.stdin.readline())
    m = s // 60
    s = s - (60 * m)
    h = m // 60
    m = m - (60 * h)
    d = h // 24
    h = h - (24 * d)
    z = f'{d}d:{h}h:{m}m:{s}s'
    return z
print(to_date())