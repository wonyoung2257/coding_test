import sys
input = sys.stdin.readline
n = int(input())

dp = [i for i in range(50001)]

for i in range(4, n+1):
  j = 1
  while j*j <=i:
    dp[i] = min(dp[i], dp[i-j*j] + 1)
    j+=1

print(dp[n])