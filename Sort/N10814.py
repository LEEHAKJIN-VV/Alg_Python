# 2020 09 09
# Made by Hakjin
# Subject: Number Sort #
import sys

n = int(input())
user=[]

for i in range(n):
    user.append(list(sys.stdin.readline().split()))

user.sort(key = lambda k: int(k[0]))

for age,name in user:
    sys.stdout.write(age + ' ' +name + '\n')
    
