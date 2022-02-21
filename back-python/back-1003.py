import sys

sys.stdin = open("./input_py.txt", "r")

T = int(sys.stdin.readline())

arr = [0] * 41
arr[0] = [1, 0]
arr[1] = [0,1]

for _ in range(T):
  testCase = int(sys.stdin.readline())
  if testCase == 0:
    print(1,0)
    continue
  if testCase == 1:
    print(0, 1)
    continue  
  
  for i in range(testCase+1):
    if arr[i] == 0:
      arr[i] = [arr[i-1][0]+arr[i-2][0], arr[i-1][1]+arr[i-2][1]]

  print(arr[testCase][0], arr[testCase][1])