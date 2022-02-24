from logging.config import valid_ident
import sys
sys.setrecursionlimit(10000)
sys.stdin = open("input_py.txt", "r")

C = int(input())
M = int(input())

def dfs(v):
  visited[v] = True

  for i in graph[v]:
    if not visited[i]:
      dfs(i)
graph = [[] for _ in range(C+1)]
visited = [False] * (C+1)

for i in range(M):
  n,v = map(int, sys.stdin.readline().split())
  graph[n].append(v)
  graph[v].append(n)

dfs(1)
cnt =0
for i in visited:
  if i:
    cnt+=1

print(cnt-1)