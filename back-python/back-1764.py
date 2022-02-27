# N 만큼 배열에 입력 받는다.
# 다시 M만큼 입력받는데 배열에 있다면 따로 입력받는다.

import sys

sys.stdin = open("input_py.txt", "r")

N, M = map(int, sys.stdin.readline().split())
N_arr = [sys.stdin.readline().strip() for _ in range(N)]
M_arr= [sys.stdin.readline().strip() for _ in range(M)]

result = list(set(N_arr) & set(M_arr))
print(len(result))
for name in sorted(result):
  print(name)