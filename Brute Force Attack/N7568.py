# 2020 09 12
# Made by Hakjin
# Subject: Brute Force Attack #

import sys
from collections import OrderedDict

n = int(sys.stdin.readline())
user = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    cnt = 1
    for j in range(n):
        if user[i][0] < user[j][0] and user[i][1] < user[j][1]:
            cnt+=1
    sys.stdout.write(str(cnt)+ ' ')
        
