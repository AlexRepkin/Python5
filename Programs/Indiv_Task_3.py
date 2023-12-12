#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант - 28. Задание № 3, пункт №6.
if __name__ == '__main__':
    pounds = int(input("Good day! How many pounds do we need to convert? - "))
    print("Very well:\n|     pounds     |       kg       |\n" + "-"*35)
    for i in range(1, pounds + 1):
        calculation = round(i * 0.4, 1)
        # print(i, "pounds are equal to ", round(i * 0.4, 1), "kg.")
        print("|", " "*(7 - len(str(i))), i, "      |", " "*(7 - len(str(calculation))),
              calculation, "      |\n" + "-"*35)
