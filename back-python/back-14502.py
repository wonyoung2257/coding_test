import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split(' '))
rap = []
temp = [[0]*M for _ in range(N)]
for i in range(N):
  rap.append(list(map(int, input().split(' '))))

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

#바이러스를 dfs로 퍼트린다.
#초기 바이러스 위치가 필요
def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0<= ny < M:
      if temp[nx][ny] ==0:
        temp[nx][ny] = 2
        virus(nx, ny)
        
def get_score():
  score = 0
  for i in range(N):
    for j in range(M):
      if temp[i][j] == 0:
        score +=1
  return score

result = 0
def dfs(count):
  global result
  if count ==3:
    for i in range(N):
      for j in range(M):
        temp[i][j] = rap[i][j]
    
    for i in range(N):
      for j in range(M):
        if temp[i][j] == 2:
          virus(i, j)
    result = max(result, get_score())
    return
  
  for i in range(N):
    for j in range(M):
      if rap[i][j] == 0:
        rap[i][j] = 1
        count += 1
        dfs(count)
        rap[i][j] = 0
        count -= 1
dfs(0)
print(result)