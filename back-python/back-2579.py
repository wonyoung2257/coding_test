import sys

sys.stdin = open("input_py.txt", "r")

T = int(input())
arr = [int(input()) for _ in range(T)]
dp = []
if T >2:
  dp.append(arr[0])
  dp.append(arr[0]+ arr[1])
  dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))

  for i in range(3,T):
    dp.append(max(dp[i-2], dp[i-3]+arr[i-1])+arr[i])

  print(dp[T-1])
else:
  if T == 1:
    print(arr[0])
  else:
    print(arr[0]+arr[1])
    
print(dp)