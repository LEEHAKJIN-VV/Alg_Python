import sys
from queue import PriorityQueue

def initData(n,x,que):
    dis=[sys.maxsize]*(n+1)
    dis[x]=0

    for i in range(1,n+1):
        que.put([dis[i],i])
    return dis,que

def dijkstra(dis,s,edge_list,que):
    while not que.empty():
        u = que.get()
        s.add(u[1])
        for i in range(j,len(edge_list)):
            if edge_list[i][0] == u[1]:
                relax(dis,u[1],edge_list[i][1],edge_list[i][2],s,que)
    return dis.copy()
    
def relax(dis,u,v,w,s,que):
    if dis[v] > dis[u]+w and not(v in s):
        dis[v] = dis[u]+w
        que.put([dis[v],v])
        
def swap_list(li):
    for i in range(1,len(li)):
        li[i][0],li[i][1] = li[i][1],li[i][0]

def main():
    n,m,x = map(int,sys.stdin.readline().split())
    edge_list=[]
    c1_dis=[]
    c2_dis=[]

    edge_list.append([-1,-1,-1])
    s=set()
    que = PriorityQueue()

    dis,que = initData(n,x,que)

    for _ in range(m):
        edge_list.append(list(map(int,sys.stdin.readline().split())))

    c1_dis = dijkstra(dis,s,edge_list,que)
    swap_list(edge_list)
    s.clear()
    dis,que=initData(n,x,que)
    c2_dis = dijkstra(dis,s,edge_list,que)
    for i in range(1,n+1):
        dis[i] = c1_dis[i]+c2_dis[i]

    sys.stdout.write(str(max(dis[1:])))

main()

