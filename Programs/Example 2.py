#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    n = int(input("Good day! We need you to give us N's value. N = "))
    if n == 1 or n == 2 or n == 12:
        print("Well, it seems to us, that Winter is outdoors!")
    elif n == 3 or n == 4 or n == 5:
        print("Well, it seems to us, that Spring is outdoors!")
    elif n == 6 or n == 7 or n == 8:
        print("Well, it seems to us, that Summer is outdoors!")
    elif n == 9 or n == 10 or n == 11:
        print("Well, it seems to us, that Autumn is outdoors!")
    else:
        print("Well, it seems to us, that ... Error! No season is found!",
              file=sys.stderr)
        exit(1)
