# 위상 정렬 시간 복잡도 O(V+E)
from collections import deque
import sys
sys.stdin = open('input_py.txt','r')

input = sys.stdin.readline

v, e = map(int, input().split())
# 진입 차수 0으로 초기화 
indegree = [0] *(v+1)

graph = [[] for i in range(v+1)]

for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)

  indegree[b] +=1

def topoloqy_sort():
  result = []
  q = deque()

  for i in range(1, v+1):
    if indegree[i] ==0:
      q.append(i)
  
  while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
      indegree[i] -= 1

      if indegree[i] ==0 :
        q.append(i)
  
  for i in result:
    print(i, end=' ')

topoloqy_sort()