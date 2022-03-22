import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())
# 2차원 리스트, 최단 거리를 저장하는 2차원 리스트
# 노드 번호화 인덱스 번호를 같게하기 위해서 n+1로 만듬
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b] =0

for _ in range(m):
  a,b,c = map(int , input().split())
  graph[a][b] = c
# K = K번 노드를 거처서 가능 경우를 계산
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print('INF', end=' ')
    else:
      print(graph[a][b], end=' ')
  print()