alphabet = "".join(
    [str(el) for el in range(10)] + [chr(el)
                                     for el in range(ord("A"), ord("Z") + 1)]
)


def decI(num: str, from_base: int):
    num = num[::-1]
    r = 0

    for pos, dig in enumerate(num):
        r += alphabet.index(dig) * from_base**pos

    return r


def decF(num: str, from_base: int):
    num = num.replace(",", ".").split(".")[1]
    r = 0.0

    for pos, dig in enumerate(num):
        r += alphabet.find(dig) * from_base ** (-pos - 1)

    return r


def convI(num: str, from_base: int, new_base: int):
    res: list[str] = []
    num = decI(num, from_base)
    while num:
        res.append(alphabet[num % new_base])
        num //= new_base
    return "".join(res[::-1])


def convF(num: str, from_base: int, new_base: int, precision: int = 10):
    res: list[str] = []
    num = decF(num, from_base)
    _ = new_base
    for _ in range(precision):
        tmp = num * new_base
        num = tmp - int(tmp)
        res.append(alphabet[int(tmp)])

    return "." + "".join(res)
