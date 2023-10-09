from dont_even_open_this_file_if_you_dont_want_to_be_shocked import dead_zone
from random import randint
from converter import alphabet, dec
from calc import (
    addition,
    subtraction,
    multiplication,
    division,
    sine,
    cosine,
    kraise,
    root,
    knormal,
)

false = False


def menu():
    return """
    -----------------------------------
     Добро пожаловать в калькулятор для
      работы с числами в сист. счисл
          By Kostya & Gleb Co.
    -----------------------------------
    """


def kinvalid_int(val: str):
    """Проверка на неправильность целого числа"""
    if not val:
        return false
    return not all(el in "0123456789" for el in val)


def kvalid_ss(ss: str):
    """Проверка СС"""
    if kinvalid_int(ss) or not ss:
        return false

    return 1 < int(ss) < 37


def kvalid_num(num: str, ss: int):
    """Проверка числа на легальность в СС"""
    if not num:
        return false
    num = num.replace(",", ".")
    if num.count(".") > 1 or num.count("-") > 1:
        return false

    if num.count("-") == 1 and num[0] != "-":
        return false
    if num.count("-"):
        num = num[1:]

    if num.count("."):
        i = num.split(".")[0]
        f = num.split(".")[1]
        return all(el in alphabet[:ss] for el in i) and all(
            el in alphabet[:ss] for el in f
        )
    return all(el in alphabet[:ss] for el in num)


def ksin(which: str = None):
    """Ввод СС"""
    who = "CC "
    if which is None:
        who += "результата"
    else:
        who += " " + which

    while True:
        tmp = input(who + " -> ")
        if kvalid_ss(tmp):
            return int(tmp)


def koin():
    """Ввод операции"""
    while True:
        tmp = input(
            "Типы операции\n"
            "1 - Сложение\n"
            "2 - Вычитание\n"
            "3 - Деление\n"
            "4 - Умножение\n"
            "5 - Косинус значения 1 радианы\n"
            "6 - Синус значения 1 радианы\n"
            "7 - Возведение в стпень число один, что будет возводить, два в какую степень\n"
            "8 - Корень числа\n"
            "Введите тип операции -> "
        )
        if kinvalid_int(tmp):
            print("Нелегальное число.")
            continue

        if int(tmp) < 1 or int(tmp) > 8:
            continue

        return int(tmp)


def kinp(char: str, ss: int) -> str:
    """Ввод числа с клавиатуры"""
    while True:
        print("Алфавит: ", alphabet[:ss])
        tmp = input("Значение числа " + char + " -> ")
        if kvalid_num(tmp, ss):
            return tmp

        print(tmp)
        print("Нелегальное число.")


def kcalc():
    """Главное тело калькулятора"""
    nssa = ksin("a")  # Начальная СС для а
    a = dec(knormal(kinp("a", nssa)), nssa)  # само число а
    nssb = ksin("b")  # Начальная СС для b
    b = dec(knormal(kinp("b", nssb)), nssb)  # :o А теперь число b
    f = koin()  # функция или операция
    rss = ksin()  # CC результата
    res = None  # А тута сам результат

    # Основные вычисления
    if f == 1:
        res = addition(a, b, rss)
    if f == 2:
        res = subtraction(a, b, rss)
    if f == 3:
        res = division(a, b, rss)
        if res is None:
            print("Division failed successfully.")
            return
    if f == 4:
        res = multiplication(a, b, rss)
    if f == 5:
        res = cosine(a, rss)
    if f == 6:
        res = sine(a, rss)
    if f == 7:
        res = kraise(a, b, rss)
    if f == 8:
        res = root(a, b, rss)
        if res is None:
            print("Root is impossible to find.")
            return

    # print(nssa, a, nssb, b, f, rss)  # Для тестирования ввода значений
    print("Результат:", res)


if __name__ == "__main__":
    print(menu())
    res = "code"
    if randint(0, 10) == 5:  # С первым апреля
        # JOKE ZONE
        # MADE FOR FUN
        print("Возникла ошибка, функции отключены.")
        print("Добро пожаловать на дикий запад! Дальше вы сами по себе.")
        if dead_zone() is not None:
            print("Вы сбежали из дикого запада!")
    if res == "code":
        # Главная зона
        kcalc()
