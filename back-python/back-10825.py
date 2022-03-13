import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
  name, k, e, m = input().strip().split(' ')
  arr.append((name, int(k), int(e), int(m)))

arr.sort(key= lambda x:(-x[1], x[2], -x[3],x[0]))

for i in arr:
  print(i[0])