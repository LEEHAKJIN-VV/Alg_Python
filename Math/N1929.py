# 2020 09 21
# Made by Hakjin
# Subject: 수학 정수론 소수 판정 에라토스테네스의 체 #

import sys,math

n = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))
data = list(filter(lambda x: x>1,data))

count=0
for i in data:
    m = int(math.sqrt(i))
    j=2
    while j<=m:
        if i%j==0:
            count+=1
            break
        j+=1
print(len(data)-count)


