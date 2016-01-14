#! /usr/bin/python3

import math
import unicodedata

def main():
    n = 1290951819840
    answer = 0

    while (n * math.log(n)) <= 3.6e13:
        n = n + 1
        answer = n
        print(n * math.log(n), "less than or equal to", 3.5e13, n)


if __name__ == "__main__": main()
