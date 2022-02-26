# N 만큼 배열에 입력 받는다.
# 다시 M만큼 입력받는데 배열에 있다면 따로 입력받는다.

import sys

sys.stdin = open("input_py.txt", "r")

N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
  arr.append(sys.stdin.readline().strip())

result = []
for i in range(M):
  name = sys.stdin.readline().strip()
  if name in arr:
    result.append(name)

result = sorted(result)
print(*result)