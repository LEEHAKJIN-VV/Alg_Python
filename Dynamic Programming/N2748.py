import sys

def fib(n,f):
    if n<=2:
        return 1
    f[1],f[2]=1,1
    for i in range(3,n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]

def main():
    n = int(sys.stdin.readline())
    f = [-1]*(n+1)
    sys.stdout.write(str(fib(n,f)))

main()