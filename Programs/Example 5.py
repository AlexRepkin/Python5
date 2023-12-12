#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


# Постоянная Эйлера.
EULER = 0.5772156649015328606
# Точность вычислений.
EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Good day! We need you to give us X's value. X = "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)
    a = x
    S, k = a, 1
    while math.fabs(a) > EPS:
        a *= x * k / (k + 1) ** 2
        S += a
        k += 1
    print(
        f"According to our calculations, Ei({x}) = {EULER + math.log(math.fabs(x)) + S}")
