def negate(a):
    return int(not (a))


def l_and(a, b):
    return int((a) and (b))


def l_or(a, b):
    return int((a) or (b))


def xor(a, b):
    return int((a) != (b))


def imply(a, b):
    return int((a) <= (b))


def equals(a, b):
    return int((a) == (b))


def nand(a, b):
    return int(not ((a) and (b)))


def nor(a, b):
    return int(not ((a) or (b)))
