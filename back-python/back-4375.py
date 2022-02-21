import sys

sys.stdin = open("./input_py.txt", "r")

# testCase = list(map(int, sys.stdin.readline().split()))
arr = []
for i in range(10000):
  num = sys.stdin.readline()
  if num == '':
    break
  arr.append(int(num))


for num in arr:
  cnt = 1
  temp = 1
  while(True):
    if temp % num ==0:
      print(cnt)
      break
    cnt+=1
    temp = temp*10 +1

for num in arr:
  temp = 1
  if temp % 2 ==0 or temp % 5 == 0: continue
  while(True):
    result = num * temp
    number1 = '1'* len(str(result))
    if result == int(number1):
      print(len(str(result)))
      break
    temp +=1