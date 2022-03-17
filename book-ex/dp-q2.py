import sys

sys.stdin = open("input_py.txt", "r")

n = int(input())
dp = []

for i in range(n):
  dp.append(list(map(int, input().split())))

for i in range(1, n):
  for j in range(len(dp[i])):
    if j == 0:
      left = 0
    else:
      left = dp[i-1][j-1]
    if j == len(dp[i]) -1:
      right = 0
    else:
      right = dp[i-1][j]
    dp[i][j] = max(left, right) + dp[i][j]
    

print(max(dp[n-1]))