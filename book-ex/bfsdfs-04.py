import sys
from collections import deque

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split(' '))
graph = []
for _ in range(N):
  graph.append(list(map(int, input().strip())))

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x,y):
  q = deque()
  q.append((x,y))
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny <M :
        if graph[nx][ny] ==0:
          continue

        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          q.append((nx,ny))
  return graph[N-1][M-1]

print(bfs(0,0))

