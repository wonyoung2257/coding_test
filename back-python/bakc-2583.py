import sys

from collections import deque

sys.stdin = open("input_py.txt", "r")

M, N ,K  = map(int, input().split())

graph = [[0]*N for _ in range(N)]

for _ in range(K):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      graph[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [ 0, 0, -1, 1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  cnt = 1
  graph[x][y] = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x+ dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= M or ny >= N:
        continue
      if graph[nx][ny] == 1:
        continue
      if graph[nx][ny] == 0:
        cnt+=1
        graph[nx][ny] = 1
        queue.append((nx, ny))
  return cnt

result = []
total = 0
for i in range(M):
  for j in range(N):
    if graph[i][j] == 0:
      total +=1
      result.append(bfs(i,j))
  
result.sort()
print(total)
print(*result)

