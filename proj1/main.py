def convI(num: int, base: int, new_base: int) -> int:
    res: list[str] = []
    num = decI(num, base)
    while num:
        res.append(str(num % new_base))
        num //= new_base
    return int("".join(res[::-1]))


def decI(num: int, base: int) -> int:
    res = 0
    for i, digit in enumerate(map(int, str(num)[::-1])):
        res += digit * base**i
    return res


def decF(num: float, base: int) -> float:
    if abs(num) < 1.0:
        res = 0.0
        str_num = str(num)[2:]
        for i, digit in enumerate(map(int, str_num)):
            res += digit * base ** (1 / (-i - 1))
        return res
    print("Only use for decimal part of number not int.")
    return -1


def convF(fl: float, base: int, new_base: int) -> float:
    return 0.0


print(decI(10100, 2), int("10100", 2))
print(convI(11, 2, 3))

print(decF(1.223, 2))
print(decF(0.1, 2))


# zoomed 5
