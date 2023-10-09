alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# alphabet = "".join(
#     [str(el) for el in range(10)] + [chr(el)
#                                      for el in range(ord("A"), ord("Z") + 1)]
# )

# Все переводы осуществляются с использованием машинного перевода
# и перевод в любую другой из другой СС осущетвляется через десятичную
#
# 4 3 2 1 0 -1 -2
# 1 1 0 0 0. 1  1 <- число
#
# 1 * 2**3 + 1 * 2**4 + 1 * 2**-1 + 1 * 2**-2
#
# И так далее :3
# !!! Все числа при переводе не в 10-ричную имеют 10 знаков после запятой -> precision


def dec(num: str, from_base: int):
    """Перевод в десятичную СС из другой"""
    return decI(num, from_base) + decF(num, from_base)


def conv(num: str, from_base: int, new_base: int):
    """Перевод числа в любую другую СС из любой другой СС"""
    return convI(num, from_base, new_base) + convF(num, from_base, new_base)


def decI(num: str, from_base: int):
    """Переводим целую часть с отрезанием минуса и дробной части"""
    m = -1 if (num[0] == "-") else 1
    num = num.replace(",", ".").split(".")[0]
    if m < 0:
        num = num[1:]
    num = num[::-1]
    r = 0

    for pos, dig in enumerate(num):
        r += alphabet.index(dig) * from_base**pos

    return m * r


def decF(num: str, from_base: int):
    """Переводим дробную часть с отрезанием целой части"""
    num = num.replace(",", ".").split(".")[1]
    r = 0.0

    for pos, dig in enumerate(num):
        r += alphabet.find(dig) * from_base ** (-pos - 1)

    return r


def convI(num: str, from_base: int, new_base: int):
    """Переводим целую часть с отрезанием минуса и дробной части"""
    m = "-" if (num[0] == "-") else ""
    if m:
        num = num[1:]
    res: list[str] = []
    num = decI(num, from_base)
    while num:
        res.append(alphabet[num % new_base])
        num //= new_base

    if not res:
        return "0"
    return m + "".join(res[::-1])


def convF(num: str, from_base: int, new_base: int, precision: int = 10):
    """Переводим дробную часть с отрезанием минуса и целой части"""
    res: list[str] = []
    num = decF(num, from_base)
    for _ in range(precision):
        tmp = num * new_base
        num = tmp - int(tmp)
        res.append(alphabet[int(tmp)])

    return "." + "".join(res)
