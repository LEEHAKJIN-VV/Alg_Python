# 2020 09 16
# Made by Hakjin
# Subject: ACM HOTEL #

import sys,math

n = int(sys.stdin.readline().rstrip())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for x in data:
    n1 = str(x[2]%x[0])
    if n1=='0':
         n1=str(x[0])
    n2 = str(math.ceil(x[2]/x[0]))
    if(len(n2)==1):
        n2 = str(0)+n2
    sys.stdout.write(n1+n2+'\n')
