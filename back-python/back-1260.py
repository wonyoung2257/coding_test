import sys
from collections import deque

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

def dfs(v):
  visitedD[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visitedD[i]:
      dfs(i)

def bfs(v):
  q = deque([v])
  visitedB[v] = True
  
  while q:
    v = q.popleft()
    print(v, end= ' ')
    for i in graph[v]:
      if not visitedB[i]:
        q.append(i)
        visitedB[i] = True

N, M, V = map(int, input().split(' '))

graph = [[] for _ in range(N+1)]
visitedD = [False] *(N+1)
visitedB = [False] *(N+1)

for i in range(M):
  arr = list(map(int, input().split(' ')))

  graph[arr[0]].append(arr[1])
  graph[arr[1]].append(arr[0]) 

for i in range(len(graph)):
  graph[i] = sorted(graph[i])

dfs(V)
print()
bfs(V)
