import sys
sys.stdin = open("input_py.txt", "r")

N = int(input())
dp = [N+1]*N
dp[0] = 0
arr = list(map(int,input().split()))

for i in range(N):
  move = arr[i]  
  for j in range(1,move+1):
    if i+j >=N:
      break
    dp[i+j] = min(dp[i+j], dp[i] + 1)
  

print(dp[N-1] if dp[N-1] != N+1 else -1)