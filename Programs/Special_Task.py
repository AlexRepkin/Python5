#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


# Вариант - 28. Задание Повышенной сложности, №1 - Интегральный синус.
if __name__ == '__main__':
    x = int(input("Good day! Please, enter x - "))
    eps = 1e-10
    a = x  # a, когда n = 0.
    cycle_sum, n = a, 0
    while math.fabs(a) > eps:
        a *= -((x**2 * (2*n + 1))/((2*n + 3)**2 * (2*n + 2)))
        cycle_sum += a
        n += 1
    print("According to our calculations, Si(", x, ") = ", cycle_sum)
