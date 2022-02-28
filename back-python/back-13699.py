n = int(input())

if n == 0 or n==1:
  print(1)
else:
  dp = [0] *(n+1)
  dp[0], dp[1] = 1, 1
  for i in range(2, n+1):
    for j in range(i):
      dp[i] += dp[j]*dp[i-j-1]

  print(dp[n])