import heapq
import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

# 거리 정보 저장 배열
distance = [INF] *(n+1)

def dijkstra(start):
  q = []

  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance)