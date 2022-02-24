import sys

from collections import deque
from unittest import result

sys.stdin = open("input_py.txt", "r")

N, M, R  = map(int, input().split())
# N 정점 수, M 간선 수, R 시작 정점

graph = [[]for _ in range(N+1)]

for i in range(M):
  u,v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
  graph[u].sort()

result = []
visited = [False] * (N+1)
def bfs(v):
  queue = deque()
  queue.append(v)
  visited[v] = True
  cnt = 0
  while queue:
    v = queue.popleft()
    result.append(v)
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

print(bfs(R))

