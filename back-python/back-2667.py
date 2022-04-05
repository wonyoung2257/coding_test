import sys
sys.stdin = open('input_py.txt','r')

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]
temp = []
# number = 2
def dfs(x,y, cnt):
  for i in range(4):
    nx = x+ dx[i]
    ny = y+ dy[i]

    if 0 <= nx < n and 0 <= ny < n:
      if graph[nx][ny] == 1:
        graph[nx][ny] = 'v'
        cnt = dfs(nx, ny, cnt+1)
  return cnt

for i in range(n):
  for j in range(n):
    if graph[i][j] != 0 and graph[i][j] != 'v':
      num = dfs(i,j, 0)
      if num == 0:
        temp.append(num+1)
      else:
        temp.append(num)
      
print(len(temp))
for i in sorted(temp):
  print(i)