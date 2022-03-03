import sys

sys.stdin = open("input_py.txt", "r")

n, m  = map(int, input().split())

result = 0
for i in range(n):
  data = list(map(int,input().split()))
  minV = min(data)
  result = max(result,minV)

print(minV)