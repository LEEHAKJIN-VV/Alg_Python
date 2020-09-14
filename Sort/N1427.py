# 2020 09 14
# Made by Hakjin
# Subject: 소트인사이드 #

import sys

n = sys.stdin.readline().rstrip()
n = [x for x in n]
n.sort(key=lambda x:x,reverse=True)
for i in n:
    sys.stdout.write(i)