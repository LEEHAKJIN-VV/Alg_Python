# 2020 09 07
# Made by Hakjin
# Alg: brute force Attack #

import sys

n = int(sys.stdin.readline())
number = 666

while n:
    if '666' in str(number):
        n -= 1
    number += 1

print(number - 1)


