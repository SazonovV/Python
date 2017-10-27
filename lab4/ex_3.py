#!/usr/bin/env python3
import math
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
#def ABSList(list):
 #   return(abs(list))
#data.sort(key = ABSList)
#print(data)
print(sorted(data, key = lambda x: math.fabs(x)))