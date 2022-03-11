def dfs(x):
  visited[x] = True
  print(x, end ='\n')
  
  for i in graph[x]:
    if not visited[i]:
      dfs(i)

graph = [ [],
[2,3,8],[1,7],[1,4,5], [3,5], [3,4], [7],[2,6,8],[1,7]
]
visited = [False]*9

dfs(1)