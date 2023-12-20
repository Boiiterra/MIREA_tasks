from math import log2, ceil


def snf(binval: str, sdnf: bool = True) -> str:
    """Default snf is sdnf.
    sdnf: 1001 -> a and not b and not c and d
    sknf: 1001 -> not a or b or c or not d"""

    tmp = []
    res = []
    ln = ceil(log2(len(binval)))

    binval += "0" * (2 ** ln - len(binval))

    alphabet = "abcdefghij"
    command = ""
    amm = 0
    appended = []

    for char in alphabet:
        amm += 1
        command += f"for {char} in range(2):\n" + "    " * amm
        appended.append(char)
        if amm == ln:
            break

    rcommand = "print('\t | "
    for ind, char in enumerate(appended):
        rcommand += f"{char}" + " | " * (ind + 1 < len(appended))
    rcommand += " | F |')"

    command += "print('\t', "
    for ind, char in enumerate(appended):
        command += f"{char}" + ", " * (ind + 1 < len(appended))
    index = "'"
    for char in appended:
        index += "{" + char + "}"
    index += "'.format("
    for ind, char in enumerate(appended):
        index += f"{char}={char}" + ", " * (ind + 1 < len(appended))
    index += ")"
    command += f", binval[int({index}, 2)], '', sep=' | ')"

    command = rcommand + "\n" + command

    print("[WARNING]: Doing unsafe stuff with exec on dynamic code.")
    exec(command)
    print()

    for ind, val in enumerate(binval):
        if int(val) == sdnf:
            nval = bin(ind)[2:]
            tmp.append("0" * (ln - len(nval)) + nval)

    res = ["" for _ in range(len(tmp))]

    mfunc = "and" if sdnf else "or"
    sfunc = "or" if sdnf else "and"

    for ind, val in enumerate(tmp):
        res[ind] += "("
        for jind, char in enumerate(val):
            if int(char) == sdnf:
                res[ind] += appended[jind] + f" {mfunc} " * (jind + 1 < len(val))
            else:
                res[ind] += f"not {appended[jind]}" + f" {mfunc} " * (
                    jind + 1 < len(val)
                )

        res[ind] += ")"
    res = f" {sfunc} ".join(res)

    return res


def demo():
    print("\nDEMO START\n\n")

    print(snf("0001000000000001", 1))
    print(snf("0001000000000001", 0))
    print(snf("10011001"))
    print(snf("10011001", 0))
    print(snf("1001"))
    print(snf("1001", 0))
    print(snf("10"))
    print(snf("10", 0))

    print("\n\nDEMO END\n")


if __name__ == "__main__":
    inp = input("Enter sequence of 0s and 1s -> ")
    fns = input("Do you want to do 1. СКНФ или 2. СДНФ? 1 or 2 -> ")

    if not fns or len(set(inp)) != 2 or not fns[0] in "12":
        demo()
        exit()

    print(snf(inp, bool(int(fns) - 1)))


