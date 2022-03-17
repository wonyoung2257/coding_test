import sys

sys.stdin = open("input_py.txt", "r")
n = int(input())
t = []
p =[]
dp= [0] *(n+1)
for i in range(n):
  x, y = map(int, input().split())
  t.append(x)
  p.append(y)

for i in range(n-1, -1, -1):
  # 상담이 끝나는 시간 계산
  time = t[i] + i

  max_v = 0
  if time <= n:
    dp[i] = max(p[i]+dp[time], max_v)
    max_v = dp[i]
  else:
    dp[i] = max_v

print(max_v)
print(dp)