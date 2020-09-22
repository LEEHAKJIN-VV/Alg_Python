import sys

n = int(sys.stdin.readline().rstrip())

if n//100==0:
    print(n)
else:
    count=0
    for i in range(100,n+1):
        i = str(i)
        if int(i[0])-int(i[1])==int(i[1])-int(i[2]):
            count+=1
    print(99+count)
        