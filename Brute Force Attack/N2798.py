# 2020 09 06
# Made by Hakjin
# Alg: brute force Attack #

import sys
from itertools import permutations
from itertools import combinations

def main():
    __,max = map(int,sys.stdin.readline().rsplit())
    min = -1
    sumD = 0

    data = []
    data = map(int,sys.stdin.readline().split())

    for i in combinations(data,3):
        sumD = sum(i)
        if(abs(max-sumD) <= abs(max-min) and sumD <= max):
            min = sumD
    
    print(min) if min != -1 else print(sumD)
main()
