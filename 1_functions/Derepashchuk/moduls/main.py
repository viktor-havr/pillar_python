import sys
# TODO:  Напиши документацію для модуля.


def to_date():
    # TODO: Зроби, щоб якщо функція отримує число, то обробляла його, а якщо не отримує агрументів, тоді вводити
    #  з клавіатури. Програма не повина падати, якщо вводять або передають не int, а попереджати, що не так
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


if __name__ == "__main__":
    # TODO: Функція нічого не виводить
    to_date()
