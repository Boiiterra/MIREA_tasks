from converter import convI, convF, decI, decF


def sep():
    return print("-" * 8)


for i in range(2, 37):
    num = ".09868632579000"
    print(f"{num} in {i} -> {convF(num, 10, i)}")
