import sys

sys.stdin = open("input_py.txt", "r")

N,K  = map(int, input().split())

dp = [[0]*(N+1) for _ in range(K+1)]

for i in range(1, K+1):
  for j in range(1, N+1):
    if i == 1:
      dp[i][j] = 1
    elif i ==2:
      dp[i][j] = j+1
    elif j == 1:
      dp[i][j] = i
    else:
      dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[K][N] % 1000000000)