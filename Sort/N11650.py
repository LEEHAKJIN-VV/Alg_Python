# 2020 09 13
# Made by Hakjin
# Subject: 좌표 정렬하기 #

import sys

n = int(sys.stdin.readline())
location = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
location.sort(key=lambda x: (x[0],x[1]))

for x in location:
    sys.stdout.write(str(x[0]) +' ' + str(x[1]) + '\n')