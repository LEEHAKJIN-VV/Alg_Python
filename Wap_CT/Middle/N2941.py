import sys

data=sys.stdin.readline().rstrip()
fil=["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in fil:
    data=data.replace(i,"#")

sys.stdout.write(str(len(data)))
