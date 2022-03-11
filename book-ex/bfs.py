from collections import deque

def bfs(v):
  q = deque([v])
  visited[v] = True
    
  while q:
    v = q.popleft()
    print(v, end= '\n')
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        q.append(i)


graph = [ [],
[2,3,8],[1,7],[1,4,5], [3,5], [3,4], [7],[2,6,8],[1,7]
]
visited = [False]*9

bfs(1)