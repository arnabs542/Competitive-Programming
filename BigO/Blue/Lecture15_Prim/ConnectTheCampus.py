# http://bigocoder.com/courses/OBLUE01/OBLUE01_LEC15/BLUE_L15P02/statement

import queue

INF = 10e9

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def prims(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))

while True:
    try:
        n = int(input())
        l = []

        graph = [[] for i in range(n)]
        visited = [False for i in range(n)]
        dist = [INF for i in range(n)]

        for i in range(n):
            x = list(map(int, input().split()))
            l.append(x)
        
        for i in range(n):
            for j in range(i+1,n):
                distance = (l[i][0] - l[j][0])**2 + (l[i][1] - l[j][1])**2
                graph[i].append(Node(j,distance**0.5))
                graph[j].append(Node(i,distance**0.5))

        q = int(input())

        for i in range(q):
            x,y = map(int, input().split())
            graph[x-1].append(Node(y-1,0))
            graph[y-1].append(Node(x-1,0))

        prims(0)
        print('%.2f'%sum(dist))
    except:
        break