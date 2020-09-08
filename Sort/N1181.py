# 2020 09 08
# Made by Hakjin
# Subject: Number Sort #

import sys
from collections import OrderedDict

n = int(input())
data = [sys.stdin.readline().rstrip() for i in range(n)]
data = list(OrderedDict.fromkeys(sorted(data,key = lambda x: (len(x), x))))

for i in data:
    sys.stdout.write(str(i)+'\n')