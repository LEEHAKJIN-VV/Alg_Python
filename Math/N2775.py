# 2020 09 19
# Made by Hakjin
# Subject: Combination #

import sys

def main():
    data=[]
    count = int(sys.stdin.readline().rstrip())

    for _ in range(count):
        n = int(sys.stdin.readline().rstrip())
        k = int(sys.stdin.readline().rstrip())
        n +=1
        k -=1
        data.append(combination(n+k,k))
    
    for i in range(count):
        sys.stdout.write(str(data[i])+"\n")

def combination(n,r):
    return 1 if  n==r or r==0 else combination(n-1,r-1)+combination(n-1,r)

main()