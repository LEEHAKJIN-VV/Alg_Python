# 2020 09 10
# Made by Hakjin
# Subject: Sort #

import sys

n = int(input())
data = [int(sys.stdin.readline().rstrip()) for i in range(n)]
data.sort()

for i in data:
    sys.stdout.write(str(i)+"\n")