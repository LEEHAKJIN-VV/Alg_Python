# 2020 09 11
# Made by Hakjin
# Subject: Brute Force Attack #

import sys

def nav(n):
    for i in range(1,n):
        if i+div(i) == n:
            return i
    return 0
def div(number):
    sn = str(number)
    sum = 0
    for i in range(len(sn)):
        sum+=int(sn[i])
    return sum

def main():
    print(nav(int(sys.stdin.readline())))

main()
