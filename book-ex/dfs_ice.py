import sys

sys.stdin = open("input_py.txt", "r")

# n, m = map(int, sys.stdin.readline().split())
n = 3
m = 3
graph = []
for i in range(n):
  graph.append(list(map(int ,input())))

def dfs(x, y):
  if x <=-1 or x >= n or y <= -1 or y >= m:
    return False
  if graph[x][y] == 0: # 아직 방문하지 않음
    graph[x][y] = 1 # 방문처리
    dfs(x-1, y) # 좌
    dfs(x, y-1) # 하
    dfs(x+1,y)  # 우
    dfs(x, y+1) # 상

    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result +=1

print(result)