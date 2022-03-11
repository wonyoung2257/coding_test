import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
limit = list(map(int, input().split(' ')))
M = int(input())
boxes = list(map(int, input().split(' ')))

limit.sort(reverse=True)
boxes.sort(reverse=True)
if max(limit) < max(boxes):
  print(-1)
else:
  time = 0
  l = 0
  b = 0
  cnt = 0
  while cnt != M:
    if limit[l] >= boxes[b]:      
      l +=1
      b +=1
      cnt+=1
    else:
      l +=1
    if l == N:
      time +=1
      l = 0

  print(time)