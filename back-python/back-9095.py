import sys

sys.stdin = open("./input_py.txt", "r")

T = int(sys.stdin.readline())

result = [0] *12
result[1] = 1
result[2] = 2
result[3] = 4

for i in range(4, 12):
  result[i] = result[i-1] + result[i-2] + result[i-3]

for i in range(T):
  num = int(sys.stdin.readline())
  print(result[num])