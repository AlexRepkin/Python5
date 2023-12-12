#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант - 28. Задание № 2, пункт №5.
if __name__ == '__main__':
    a = float(input("Good day! Please, enter coordinates of A, a - "))
    b = float(input("And now b - "))
    useful = a * a + b * b
    if 1 > useful > 0.25:
        print("Yep! It's somewhere between 1 and 0.25.")
    elif 1 == useful or useful == 0.25:
        print("Oof! It's exactly on a border of given ring!")
    else:
        print("Oops! It's not inside.")
