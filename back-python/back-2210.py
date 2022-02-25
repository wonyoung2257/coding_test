import sys
sys.setrecursionlimit(10000)
sys.stdin = open("./input_py.txt", "r")

graph = [input().split() for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [ 0, 0, -1, 1]
arr = []

def dfs(x,y, st):
  
  if x<0 or y<0 or x>=5 or y >=5: return
  
  st += graph[x][y]
  if len(st) == 6:
    if st not in arr:
      arr.append(st)
    return
  
  for i in range(4):
    dfs(x+dx[i], y + dy[i], st)

st = ''
for i in range(5):
  for j in range(5):
    dfs(i, j, st)
print(len(arr))