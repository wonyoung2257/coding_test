import sys
sys.setrecursionlimit(10000)
sys.stdin = open("input_py.txt", "r")

def dfs(v):
  visited[v] = True  
  for i in graph[v]:
    if not visited[i]:
      dfs(i)

N, M  = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(M):
  u, v  = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(1, N+1):
  if not visited[i]:
    dfs(i)    
    cnt +=1

print(cnt)