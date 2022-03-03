import sys

sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline
N, K = map(int, input().split())
arr = []
for _ in range(N):
  temp = int(input())
  if temp <=K: arr.append(temp)

cnt = 0
idx = len(arr) -1
while K > 0:
  cnt += K //arr[idx]
  K %= arr[idx]
  idx-=1
print(cnt)