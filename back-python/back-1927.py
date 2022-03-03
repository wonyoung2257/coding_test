from cmath import isnan
import sys
from queue import PriorityQueue

sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
que= PriorityQueue()


for i in range(N):
  num = int(input())
  if num == 0:
    if que.qsize() ==0:
      print(0)
    else:
      print(que.get())
  else:
    que.put(num)