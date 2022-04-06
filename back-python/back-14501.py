import sys
sys.stdin = open("input_py.txt", "r")

n = int(input())
t = []
p = []
for _ in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)

temp = [0]*n
for i in range(n-1, -1, -1):
  if t[i] + i <= n:
    # p[i] # 오늘일한거
    # temp[t[i]+i] # 오늘 일을 마친 날짜의 최고 소득
    if t[i] + i == n:
      temp[i] = max(p[i], max(temp))
    else:
      temp[i] = max(p[i] + temp[t[i]+i], max(temp))
  else:
    temp[i] = max(temp)

print(temp[0])