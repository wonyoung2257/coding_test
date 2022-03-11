import sys
from collections import deque


sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

def dfs(x,y):
  if 0 <= x < N and 0 <= y < M and graph[x][y] == '0':
    graph[x][y] = '1'
    
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False

N, M = map(int, input().split(' '))

graph = [list(input().strip())for _ in range(N)]

cnt = 0
for i in range(N):
  for j in range(M):
    if dfs(i,j):
      cnt+=1
print(cnt)