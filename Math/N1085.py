# 2020 09 20
# Made by Hakjin
# Subject: 수학,기하학 #

import sys,math

x,y,w,h = map(int,sys.stdin.readline().rstrip().split())

sys.stdout.write(str(min(w-x,h-y,x,y)))

