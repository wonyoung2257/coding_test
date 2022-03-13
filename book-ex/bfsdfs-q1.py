import sys
from collections import deque

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

# N 도시 수, M 도로 수, K 거리 정보 X 출발 도시
N, M, K, X = map(int, input().split(' '))

distance = [-1] * (N+1)
distance[X] = 0
city = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split(' '))
  city[a].append(b)

q = deque([X])
while q:
  now = q.popleft()

  for next_city in city[now]:
    if distance[next_city] == -1:
      distance[next_city] = distance[now]+1
      q.append(next_city)

if K not in distance:
  print(-1)
else:
  for i in range(N+1):
    if distance[i] == K:
      print(i)
