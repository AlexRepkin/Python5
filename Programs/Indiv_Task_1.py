#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


# Вариант - 28. Задание № 1, пункт №2.
if __name__ == '__main__':
    month = int(input("Good day! Which month you want us to analise? Month - "))
    if 1 > month or month > 12:
        print("Oops! There is no such a month!", file=sys.stderr)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("Very well, answer is - 30.")
    elif month == 2:
        print("Oof... There are two variants, in February it can be 28 or 29 days.")
    else:
        print("Very well, answer is - 31.")
