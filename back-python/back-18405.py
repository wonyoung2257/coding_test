import sys
from collections import deque

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]

t_s, t_x, t_y = map(int, input().split(' '))

virus = []
for i in range(n):
  for j in range(n):
    if graph[i][j] != 0:
      virus.append((graph[i][j],0,i,j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 숫자가 낮은 바이러스 부터 실시
virus.sort()
q = deque(virus)

while q:
  v_num, s, x, y = q.popleft()
  if s == t_s:
    break
  
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0<= nx < n and 0<= ny < n:
      if graph[nx][ny] ==0:
        graph[nx][ny] = v_num
        q.append((v_num,s+1,nx,ny))

print(graph[t_x-1][t_y-1])