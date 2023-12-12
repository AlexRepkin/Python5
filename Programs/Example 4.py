#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


if __name__ == '__main__':
    a = int(input("Good day! We need you to give us A's value. A = "))
    if a < 0:
        print("Excuse us, but we can't accept this value!", file=sys.stderr)
        exit(1)
    else:
        x = 1
        eps = 1e-10  # 10^(-10)
        while True:
            xp = x
            x = (x + a / x) / 2
            if math.fabs(x - xp) < eps:
                break
        print(
            f"It seems to us that in this case x = {x}. Using sqrt we got answer: sqrt(a) = {math.sqrt(a)}.")
