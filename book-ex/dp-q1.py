import sys

sys.stdin = open("input_py.txt", "r")

T = int(input())
for _ in range(T):
  n, m = map(int, input().split(' '))
  temp = list(map(int, input().split(' ')))
  arr = [[]for _ in range(n)]

  for i in range(n):
    for j in range(m):
      arr[i].append(temp.pop(0))
  
  dp = [[-1]*m for _ in range(n)]
  for i in range(n):
    dp[i][0] = arr[i][0]
  dx = [1,0,-1]
  result = -1
  for y in range(1,m):
    for x in range(n):
      # 한 단계 전의 값과 현재 x, y 값을 더한다
      # 한 단계 전의 왼쪽 위, 왼쪽, 왼쪽 아래 중 큰 값을 더한다.
      max_num = -1
      for i in range(3):
        nx = x + dx[i]
        ny = y -1
        if 0 <= nx < n:
          max_num = max(max_num, dp[nx][ny])
      dp[x][y] = max_num + arr[x][y]
      result = max(result,dp[x][y])
  print(result)