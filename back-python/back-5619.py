# 왜 4개 까지 하면 맞는것인가??
from itertools import permutations
import sys
import heapq
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n = int(input())
h = []
for i in range(n):
  num = int(input())
  if len(h)<4:
    heapq.heappush(h, -num)
  else:
    if num < h[0]*-1:
      heapq.heappop(h)
      heapq.heappush(h, -num)

temp = []
for n in h:
  temp.append(str(-n))
temp = list(permutations(temp, 2))

answer = []
for a, b in temp:
  answer.append(int(a+b))
answer.sort()
print(answer[2])