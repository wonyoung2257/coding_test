import sys

sys.stdin = open('input_py.txt','r')
input = sys.stdin.readline

n = int(input())
arr = []


for _ in range(n):
  r, g, b = map(int, input().split())
  arr.append([r, g, b])

for i in range(1, n):
  arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
  arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
  arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]


print(min(arr[n-1][0], arr[n-1][1], arr[n-1][2]))

