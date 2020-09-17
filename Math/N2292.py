# 2020 09 16
# Made by Hakjin
# Subject: Math
# 벌집계산 문제 #

import sys

r = int(sys.stdin.readline().rstrip())

for i in range(1000000000):
    if r==1:
        print(1)
        break
    if 3*(i**2+i)+1 < r <= 3*((i+1)**2+(i+1))+1:
        sys.stdout.write(str(i+2))
        break

