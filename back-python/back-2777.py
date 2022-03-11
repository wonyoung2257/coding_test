import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

T = int(input())

for i in range(T):
  arr = []
  # N = int(input())
  N = 100000001
  d = 2
  while d <= N:
    if N%d == 0:
      arr.append(d)
      N = N/d
    else:
      d+=1
  print(arr)

