import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
if N == 1:
  print(0)
else:
  num1 = int(input())
  arr = [int(input()) for _ in range(N-1)]
  arr.sort(reverse=True)
  cnt = 0
  while num1 <= arr[0]:
    num1+=1
    arr[0] -=1
    cnt+=1
    arr.sort(reverse=True)

  print(cnt)