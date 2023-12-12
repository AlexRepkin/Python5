#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    x = int(input("Good day! We need you to give us X's value. X = "))
    if x <= 0:
        print("X <= 0. It means, that Y = ", (2 * x * x) + math.cos(x))
    elif x < 5:
        print("X < 5. It means, that Y = ", x + 1)
    else:
        print("X >= 5. It means, that Y = ", math.sin(2 * x) - (x * x))
