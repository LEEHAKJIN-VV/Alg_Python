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