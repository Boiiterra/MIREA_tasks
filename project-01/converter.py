alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# alphabet = "".join(
#     [str(el) for el in range(10)] + [chr(el)
#                                      for el in range(ord("A"), ord("Z") + 1)]
# )


def dec(num: str, from_base: int):
    return decI(num, from_base) + decF(num, from_base)


def conv(num: str, from_base: int, new_base: int):
    return convI(num, from_base, new_base) + convF(num, from_base, new_base)


def decI(num: str, from_base: int):
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
    num = num.replace(",", ".").split(".")[1]
    r = 0.0

    for pos, dig in enumerate(num):
        r += alphabet.find(dig) * from_base ** (-pos - 1)

    return r


def convI(num: str, from_base: int, new_base: int):
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
    res: list[str] = []
    num = decF(num, from_base)
    for _ in range(precision):
        tmp = num * new_base
        num = tmp - int(tmp)
        res.append(alphabet[int(tmp)])

    return "." + "".join(res)
