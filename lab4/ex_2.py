#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a','b','Abc','abc','aBc']

# Реализация задания 2
#print(list(Unique(data1, ignore_case = True)))
#print(list(Unique(data2, ignore_case = True)))
print(list(Unique(data3, ignore_case=False)))