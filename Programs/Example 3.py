#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    s = 0
    n = int(input("Good day! We need you to give us N's and X's values. N = "))
    x = float(input("Great, and X = "))
    for k in range(1, n + 1):
        s += math.log(k * x) / (k * k)
    print("According to X's and N's values, S = ", s)
