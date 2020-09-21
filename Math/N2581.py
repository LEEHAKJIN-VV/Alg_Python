# # 2020 09 21
# # Made by Hakjin
# # Subject: 수학 정수론 소수 판정 에라토스테네스의 체 #

import sys,math

def prime(n,m):
    sum =0 
    data =[]
    for i in range(n,m+1):
        k = int(math.sqrt(i))
        j=2
        while j<=k:
            if i%j==0:
                break
            j+=1
        if j==k+1:
            data.append(i)
            sum+=i
    return sum,data
def main():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())

    if n==1:
        n+=1
    sum,data=prime(n,m)
    print(sum,data[0],sep="\n") if len(data)!=0 else print(-1)

main()

