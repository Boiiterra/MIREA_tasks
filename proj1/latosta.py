# La tosta
alphebet = [*map(str, range(10))] + [chr(el)
                                     for el in range(ord("A"), ord("Z") + 1)]
print("".join(alphebet)[:16])

n = "ABCDES"
ss = 16

if all(el in alphebet[:ss] for el in n):
    print("NORM")

# -----------------------------------------------

a = input("INP -> ").replace(",", ".")


def test_num(inp: str, decimal: bool):
    try:
        nn = float(a)
        n = int(nn)
        if not decimal and nn - n != 0:
            return False
        return True
    except ValueError as e:
        print("FUCKED UP\n", e)


test_num(a, False)
