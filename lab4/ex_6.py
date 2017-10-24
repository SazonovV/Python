#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = 'data_light.json'

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return sorted(list(field(arg, "job-name")),key = str.lower)


@print_result
def f2(arg):
    return list(filter(lambda x: x[0:11].lower() == 'программист', arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python",arg))


@print_result
def f4(arg):
    money = list(map(lambda x: "зарплата " + str(x),gen_random(100000, 200000, len(arg))))
    return list(zip(arg,money))


with timer():
    f4(f3(f2(f1(data))))
