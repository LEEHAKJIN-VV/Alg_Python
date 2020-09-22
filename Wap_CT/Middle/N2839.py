import sys

n = int(sys.stdin.readline().rstrip())
count=0
while True:
    if n%5==0:
        sys.stdout.write(str(count+n//5))
        break
    elif n<0:
        sys.stdout.write(str(-1))
        break
    else:
        n=n-3
        count+=1
        
