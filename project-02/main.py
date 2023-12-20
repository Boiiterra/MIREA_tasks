"""Some logic calculator, to suffer"""
from subprocess import Popen, PIPE, call
from sys import platform

# My little lib -> Используется в генераторе кода
from blogic_lib import negate, l_and, l_or, xor, imply, equals, nand, nor

from snf import snf
from gleb import gleb_snf

ALPHABET = "".join(map(chr, range(97, 123)))
INFO = "[INFO]: "


def f(e: bool) -> int:
    """Convert bool to int"""
    return int(e)


def separator():
    """Separates rows in bhelp truth table."""
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
    """Python has built-in function help. So now it is my help - bhelp.
    Print extra information about function symbols."""
    print("If you give a variables 'x' and 'y':")
    separator()
    print(
        "| x | y | not x | x or y | x and y | x xor y |",
        "x imp y | x eq y | x nand y | x nor y |",
    )
    separator()
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
            separator()
    print()


def parentheses(inp: str) -> str:
    """Swap and check parentheses"""
    for p in ["[", "{", "("]:
        inp = inp.replace(p, " ( ")
    for p in ["}", "]", ")"]:
        inp = inp.replace(p, " ) ")

    if inp.count("(") != inp.count(")"):
        return None

    return inp


def translate(inp: str) -> str:
    """From letters to symbols:
    nor          ->  '-'
    nand         ->  '|'
    xor          ->  '/'
    implication  ->  '.'
    equality     ->  '='
    or           ->  '+'
    and          ->  '*'
    not          ->  '!'
    """

    inp = " " + " ".join(inp.split()) + " "  # Add some more whitespace
    inp = inp.replace(" nor ", " - ")
    inp = inp.replace(" nand ", " | ")
    inp = inp.replace(" xor ", " / ")
    inp = inp.replace(" imp ", " . ")
    inp = inp.replace(" eq ", " = ")
    inp = inp.replace(" or ", " + ")
    inp = inp.replace(" and ", " * ")
    inp = inp.replace(" not ", " ! ")

    return inp


def strip(inp: str) -> tuple:
    """Make all variables one letter long"""

    variables = set()

    # Get all variables in provided input
    for sub_inp in inp.split():
        # print(sub_inp, all(el in ALPHABET for el in sub_inp)) # DEBUG
        if all(el in ALPHABET for el in sub_inp):
            variables |= {sub_inp}

    if len(variables) > 6:
        print("ERROR: amount of variables is HUGE.")
        return None

    variables = sorted(variables)

    for ind, var in enumerate(variables):
        replaced = False
        if len(var) == 1:  # Ignore letters
            continue
        for char in ALPHABET:  # We look for free letter to swap variable with
            if char in variables:
                continue
            variables[ind] = char
            inp = inp.replace(var, char)
            replaced = True
            break
        if not replaced:  # If we have more variables than 26
            print("[ERROR]: ran out of variables. Exceeded variable limit of 26.")
            return None

    return inp, variables


def get_string(from_: str) -> list:
    """Calls magical black box that transforms input into logical expression in prefix notation.
    Infix  notation: a + b
    Prefix notation: + a b"""
    if platform == "linux":
        p = Popen(["./logexan-exe-linux", from_], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    else:
        p = Popen(["./logexan-win.exe", from_], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    rc = p.returncode

    return [output, err, rc]


def constructor(function: str, variables: list[str]) -> str:
    """Construct python code for expression from given function.
    '(+ a b)' -> 'l_or(a, b)'
          '0' -> '0'"""
    operators = {
        "!": "negate",
        "*": "l_and",
        "+": "l_or",
        "=": "equals",
        ".": "imply",
        "/": "xor",
        "|": "nand",
        "-": "nor",
    }

    # Check if we have some actions to do. Like: and, or, not
    # If we have some, than create valid python code:
    # "(+ a b)" -> "l_or(a, b)"
    if function[0] == "(" and function[-1] == ")":
        function = "".join(function.split())  # Remove whitespace
        function = function.replace("(", ", (")
        function = function.replace(")", "), ")

        # Add commas after variables and constants
        for var in variables:
            function = function.replace(var, f"{var},")
        function = function.replace("0", "0,")
        function = function.replace("1", "1,")

        # Swap operators with corresponding functions
        for operator, func in operators.items():
            function = function.replace(f"({operator}", f"{func}(")

        # Remove commas from start and end of the expression
        # ", l_or(, a, b, ), " -> "l_or(, a, b, )"
        if function[-2:] == ", ":
            function = function[:-2]
        if function[:2] == ", ":
            function = function[2:]

        function = "".join(function.split())  # Remove whitespace
        # Remove useless items
        function = function.replace("(,", "(")
        function = function.replace(",,", ",")
        function = function.replace(",)", ")")

    return function


def process(function: str, variables: list[str]):
    """Generate code based on given function.
    Example:
    function = '(+ (* a b) a)', variables = ['a', 'b']

    Generated code:
    print(' | a | b | F | ')

    for a in range(2):
        for b in range(2):
            print('', a, b, l_or(l_and(a, b), a), '', sep=' | ')
    """
    vector = []

    command = "print(' | "
    for ind, var in enumerate(variables):
        command += f"{var}" + " | " * (ind + 1 < len(variables))
    command += " | " * (len(variables) > 0) + "F | ')\n\n"

    result = constructor(function, variables)
    for ind, var in enumerate(variables):
        command += f"for {var} in range(2):\n" + "\t" * (ind + 1)

    command += (
        "print('', "
        + ", ".join(variables)
        + ", " * (len(variables) > 0)
        + result
        + ", '', sep=' | ')"
    )

    command += "\n" + "\t" * len(variables) + f"vector.append(str({result}))"

    exec(command)

    vector = "".join(vector)

    return vector


def valid(inp: str) -> bool:
    return all(
        (char in ALPHABET) or (char in " ()") or (char == "1") or (char == "0")
        for char in inp
    )


def transform(inp: str, variables: list[str]) -> str:
    """Using some laws we transform the input to make it a little shorter
       Преобразование вырожения согласно некоторым законам алгебры логики"""
    inp = "".join(inp.split())
    inp = inp.replace("!0", "1")
    inp = inp.replace("!(0)", "1")
    inp = inp.replace("!1", "0")
    inp = inp.replace("!(1)", "0")

    inp = inp.replace("0*0", "0")
    inp = inp.replace("0*1", "0")
    inp = inp.replace("1*0", "0")
    inp = inp.replace("1*1", "1")

    inp = inp.replace("0+0", "0")
    inp = inp.replace("0+1", "1")
    inp = inp.replace("1+0", "1")
    inp = inp.replace("1+1", "1")

    for var in variables:
        inp = inp.replace(f"{var}+{var}", f"{var}")
        inp = inp.replace(f"{var}*{var}", f"{var}")

        inp = inp.replace(f"!(!{var})", f"{var}")

        inp = inp.replace(f"{var}*!{var}", "0")

        inp = inp.replace(f"{var}+1", "1")
        inp = inp.replace(f"1+{var}", "1")

        inp = inp.replace(f"{var}+0", f"{var}")
        inp = inp.replace(f"0+{var}", f"{var}")

        inp = inp.replace(f"0*{var}", "0")
        inp = inp.replace(f"(0)*{var}", "0")
        inp = inp.replace(f"{var}*0", "0")
        inp = inp.replace(f"{var}*(0)", "0")

        inp = inp.replace(f"{var}*1", f"{var}")
        inp = inp.replace(f"{var}*(1)", f"{var}")
        inp = inp.replace(f"1*{var}", f"{var}")
        inp = inp.replace(f"(1)*{var}", f"{var}")

        inp = inp.replace(f"({var})", f"{var}")
        inp = inp.replace("(1)", "1")
        inp = inp.replace("(0)", "0")

        inp = inp.replace(f"{var}.1", "1")
        inp = inp.replace(f"{var}.0", f"!{var}")

    return inp


def calc() -> list:
    functions = ["and", "or", "not", "xor", "imp", "eq", "nor", "nand"]
    print(f"{INFO}Allowed symbols for functions: ", end="")
    for i, func in enumerate(functions):
        print(f"'{func}'", end=(", " if i + 1 < len(functions) else "\n"))
    print(f"{INFO}Using other symbols may result in error.")
    print(
        f"{INFO}Separate functions and variables using "
        "spaces or else I don't know what will happen."
    )
    print(f"{INFO}Up to 6 variables supported. Constants are not variables")
    print(
        f"{INFO}If variable is longer than a symbol it will "
        "be renamed. Sorry for doing that."
    )
    print(f"{INFO}Symbols like !-$#@%^&* are not supported!")
    print(f"{INFO}Allowed input: 1 and variable")
    print(f"{INFO}Not allowed: x1 + variable_one")
    print(f"{INFO}Double negation: not (not a)")
    print(
        f"{INFO}This calculator may fail in some cases please be nice to it. It is doing it's best."
    )
    print()

    bhelp()

    print(f"{INFO}To exit input just press Enter.")
    inp = input("Please enter your funciton here -> ").lower()
    if not inp:
        print("Program finished")
        return [-1, None]

    # print(inp)
    if not valid(inp):
        print(f"{INFO}Allwed input: 1 and variable")
        print(f"{INFO}Not allwed: x1 + variable_one")
        print("[ERROR]: Illegal combination found.")
        return [1, None]

    if all(el in "01" for el in inp):
        print("Если длинна вектора меньше необходимой, то ПРИ ИСПОЛЬЗОВАНИИ")
        print("функиций помеченных GOOD нехватающие значения будут заполнены нулями!")
        return [0, inp]

    print()
    print("Your  function  :", inp)

    inp = parentheses(inp)
    if inp is None:
        print("[ERROR]: Some parentheses are missing.")
        return [1, None]

    inp = translate(inp)
    tmp = strip(inp)
    print("Your  expression:", inp)
    if tmp is None:
        return [2, None]

    inp, variables = tmp
    for _ in range(5):
        # Transform function three times. In case something is missed
        inp = transform(inp, variables)

    inp = " ".join(inp.split())  # Normalize

    output, err, rc = get_string(inp)
    output = output.decode().split("\n")[1]
    if err:
        error = err.decode().split("\n")[1]
        print(f"[ERROR]: {error}, return code: {rc}.")
        print("[ERROR]: Invalid function provided.")
        return [int(rc), None]

    print("Final expression:", inp)
    print()

    if not err:
        print(
            "[WARNING]: This is unsafe! I am about to execute generated code "
            "to display truth table!\n"
        )
        return [0, process(output, variables)]


if __name__ == "__main__":
    doing = True
    run = True

    while doing:
        if run:
            run = not run
            res = calc()
            if res[0] is None:
                print("System failed somewhere. Something illegal happened.")
                print("Try again please. Maybe do something else.")
            elif res[0] > 0:
                print("\nSome fatal error happened. Try something else.")
            elif res[0] == -1:
                print("Exiting")
                break

            if (res[1]):
                print()
                print("Получен вектор:", res[1])
                print()
                print("Что нужшно сделать дальше?")
                print("1. Совершенные формы")
                print("0. Ничего")

                inp = None
                while True:
                    inp = input()

                    if (inp in "01" + ("2" if (len(res[1]) == 8 or len(res[1]) == 16) else "") and inp):
                        break

                inp = int(inp)

                if not inp:
                    print("Пока пока.")

                if inp == 1:
                    while True:
                        print()
                        print("В какую совершенную форму преобразовать выражение?")
                        print("1. Дизъюнктивную (GOOD)")
                        print("2. Конъюнктивную (GOOD)")
                        print("4. Дизъюнктивную (Устаревшая и неправильная)")
                        print("5. Конъюнктивную (Устаревшая и неправильная)")
                        print("При использовании устаревшего кода стабильность и работоспособность не гарантируется.")

                        inp = input("Your input -> ")

                        if (not inp):
                            continue

                        if (inp in "12"):
                            inp = int(inp) - 1
                            print("Выбрана", "дизъюнктивная" if not inp else "конъюнктивная", "форма")
                            print(snf(res[1], not inp))
                            break

                        if (inp in "45"):
                            inp = int(inp) - 4
                            print("Используется устаревшая технология")
                            print("Выбрана", "дизъюнктивная" if not inp else "конъюнктивная", "форма")
                            gleb_snf(res[1], "pcnf" if inp else "pdnf")
                            break

                        print("INVALID INPUT")


        print("У вас одна попытка. Стабильность не гарантирована.")
        lato = input("Минимальные формы? y/N -> ")
        if (lato.lower() == "y"):

            yn = False
            while True and 0:
                yn = input("Таблица вбивается: Лапками? ")

                if (not yn):
                    break

                print("NOPE I WON'T LET YOU OUT")

            print("Добро пожаловать на минимальную тропу.")
            if (yn):
                call(["python", "min_gleb_auto.py"])
            else:
                call(["python", "min_gleb.py"])

        a = input("\nDo you want to continue? Y/n -> ")
        if (not a) or a.lower()[0] == "y":
            run = True
        elif a.lower()[0] == "n":
            print("Program finished.")
            print("Exiting")
            doing = not doing
        else:
            print("Invalid input try again.")
