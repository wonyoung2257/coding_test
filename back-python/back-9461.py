import sys
sys.stdin = open("input_py.txt", "r")
T = int(input())

dp = [0]*101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1,1,1,2,2


for i in range(T):
  N = int(input())
  if N <6:
    print(dp[N])
    continue
  for i in range(6, N+1):
    if dp[i] !=0:
      continue
    dp[i] = dp[i-1] + dp[i-5]
  print(dp[N])