import sys
from collections import deque

sys.stdin = open("../input_py.txt", "r")

testCase = int(sys.stdin.readline())

for i in range(testCase):
  n, m = map(int, sys.stdin.readline().split())
  arr = deque(map(int,sys.stdin.readline().split())) 
  
  cnt= 0
  point = m
  while(True):
    maxNum = max(arr)

    if arr[0] != maxNum:
      # 우선순위가 낮은 요소 맨뒤로 보냄
      arr.append(arr.popleft())   
      if point > 0:
        point -= 1
        continue
      if point == 0 or point <0:
        point = len(arr) -1

    else:
      arr.popleft()
      cnt+= 1
      if point == 0:
        print(cnt)
        break
      else:
        point -= 1
    


