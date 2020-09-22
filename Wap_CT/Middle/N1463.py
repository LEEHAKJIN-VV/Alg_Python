# import sys
# sys.setrecursionlimit(10**6)

# def one(n):
#     if n==1:
#         return 1
#     elif n<=0:
#         return 0 
#     else:
#         return 1+min(one(n//3),one(n//2),one(n-1))

# def main():
#     n = one(int(sys.stdin.readline().rstrip()))
#     print(n)

# main()

import sys
sys.setrecursionlimit(10**6)

def one(n):
    if n==1:
        return 0
    if n<=0:
        return 0  
    if data[n]>-1:
        return data[n]
    else:
        if n%3==0 and n%2==0:
            data[n]=1+min(one(n//3),one(n//2))
        elif n%3==0:
            data[n] = 1+min(one(n//3),one(n-1))
        elif n%2==0:
            data[n] = 1+min(one(n//2),one(n-1))
        else:
            data[n] = 1+one(n-1)
        return data[n]

def main():
    global data
    n = int(sys.stdin.readline().rstrip())
    data = [-1 for _ in range(n+1)]
    sys.stdout.write(str((one(n))))

main()
