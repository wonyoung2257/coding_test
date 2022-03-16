import sys
from collections import deque
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n, l, r = map(int, input().split(' '))

graph = [list(map(int ,input().split(' '))) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1,-1]

def bfs(x,y, index):
  united = []
  united.append((x,y))

  union[x][y] = index
  
  q = deque()
  q.append((x,y))
  
  population = graph[x][y]
  
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < n and 0 <= ny <n and union[nx][ny] == -1:
        if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
          population += graph[nx][ny]
          united.append((nx,ny))
          union[nx][ny] = index
          q.append((nx,ny))

  for i, j in united:
    graph[i][j] = population //len(united)
  return 

result = 0
while True:
  # 연합의 번호
  index = 0
  union = [[-1]*n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if union[i][j] == -1:
        # 연합을 만드는 함수 실행
        bfs(i,j, index)
        index+=1
  # 모든 국가가 개인 연합일때
  if index == n*n:
    break
  result +=1

print(result)