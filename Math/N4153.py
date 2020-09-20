# 2020 09 20
# Made by Hakjin
# Subject: 피타고라스의 공식 #

import sys

while True:
    n=sorted(list(map(int,sys.stdin.readline().rstrip().split())))
    if n.count(0)>0:
        break
    else:
        print("right") if n[0]**2+n[1]**2==n[2]**2 else print("wrong")
