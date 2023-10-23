"""Some logic calculator, to suffer"""


def f(e: bool) -> int:
    return int(e)


def sep():
    print(
        "+---",
        "+---",
        "+-------",
        "+--------",
        "+---------",
        "+---------",
        "+---------",
        "+--------",
        "+----------",
        "+---------+",
        sep="",
    )


def bhelp():
    """Python has built-in function help. So now it is my help - bhelp."""
    print("If you give a variables 'x' and 'y':")
    sep()
    print(
        "| x | y | not x | x or y | x and y | x xor y |",
        "x imp y | x eq y | x nand y | x nor y |",
    )
    sep()
    r = [False, True]
    for x in r:
        for y in r:
            print(
                f"| {f(x)} "
                f"| {f(y)} "
                f"|   {f(not x)}   "
                f"|    {f(x or y)}   "
                f"|    {f(x and y)}    "
                f"|    {f(x != y)}    "
                f"|    {f(not (x) or y)}    "
                f"|    {f(x == y)}   "
                f"|     {f(not(x and y))}    "
                f"|    {f(not(x or y))}    "
                f"|"
            )
            sep()
    print()


def parantecies(inp):
    for p in ["[", "{"]:
        inp = inp.replace(p, "(")
    for p in ["}", "]"]:
        inp = inp.replace(p, ")")
    return inp


def main():
    functions = ["and", "or", "not", "xor", "imp", "eq", "nor", "nand"]
    print("Allowed symbols for functions: ", end="")
    for i, func in enumerate(functions):
        print(f"'{func}'", end=(", " if i + 1 < len(functions) else "\n"))

    bhelp()

    inp = input("Please enter your funciton here -> ")
    if inp == "exit":
        print("Program finished")
        return

    inp = parantecies(inp)
    print(inp)


if __name__ == "__main__":
    main()
