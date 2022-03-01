import sys
sys.stdin = open("input_py.txt", "r")

T = int(input())
dp = [0] *10001
dp[1] = 1
dp[2] = 1
for i in range(3, len(dp)):
  dp[i] = dp[i-1] + dp[i-2]

for i in range(T):
  P, Q = list(map(int, input().split()))
  M = dp[P] % Q
  print(f'Case #{i+1}: {M}')