import sys
import heapq

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
  heapq.heappush(heap, int(input()))

answer = []
while len(heap) != 1:
  temp = heapq.heappop(heap) + heapq.heappop(heap)
  answer.append(temp)
  heapq.heappush(heap,  temp)

print(sum(answer))