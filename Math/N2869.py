# 2020 09 15
# Made by Hakjin
# Subject: 달팽이는 올라가고싶다 #

import sys

a,b,v = map(int,sys.stdin.readline().rsplit())
day = (v-b)/(a-b) if (v-b) % (a-b)==0 else (v-b)/(a-b)+1
day = int(day)
sys.stdout.write(str(day))
