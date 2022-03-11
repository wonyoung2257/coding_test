import sys
from collections import deque

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split(' '))
graph = [] # 전체 보드 정보
data = [] # 바이러스 정보

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      # 바이러스 종류, 시간, 위치x, 위치y
      data.append((graph[i][j], 0, i ,j))

s, x, y = map(int, input().split(' '))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
data.sort()
q = deque(data)

while q:
  virus, time, nowX, nowY = q.popleft()

  if time == s:
    break
  for i in range(4):
    nx = nowX + dx[i]
    ny = nowY + dy[i]

    if 0<= nx <n and 0 <= ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s+1, nx,ny))

print(graph[x-1][y-1])