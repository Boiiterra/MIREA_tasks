from converter import conv
from math import cos, sin


def knormal(num: str):
    num = num.replace(",", ".")
    if "." in num:
        return num
    return num + ".0"


def addition(a, b, rss: int):
    c = a + b
    if c < 0:
        return "-" + conv(knormal(str(-c)), 10, rss)
    return conv(knormal(str(c)), 10, rss)


def subtraction(a, b, rss: int):
    c = a - b
    if c < 0:
        return "-" + conv(knormal(str(-c)), 10, rss)
    return conv(knormal(str(c)), 10, rss)


def multiplication(a, b, rss: int):
    c = a * b
    if c < 0:
        return "-" + conv(knormal(str(-c)), 10, rss)
    return conv(knormal(str(c)), 10, rss)


def division(a, b, rss: int):
    if b == 0:
        return None
    c = a / b
    if c < 0:
        return "-" + conv(knormal(str(-c)), 10, rss)
    return conv(knormal(str(c)), 10, rss)


def sine(a, rss):
    c = sin(a)
    if c < 0:
        return "-" + conv(knormal(str(-c)), 10, rss)
    return conv(knormal(str(c)), 10, rss)


def cosine(a, rss):
    c = cos(a)
    if c < 0:
        return "-" + conv(knormal(str(-c)), 10, rss)
    return conv(knormal(str(c)), 10, rss)


def kraise(a, b, rss):
    c = a**b
    if c < 0:
        return "-" + conv(knormal(str(-c)), 10, rss)
    return conv(knormal(str(c)), 10, rss)


def root(a, b, rss):
    if b == 0:
        return None
    c = a ** (1 / b)
    if c < 0:
        return "-" + conv(knormal(str(-c)), 10, rss)
    return conv(knormal(str(c)), 10, rss)
