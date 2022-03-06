import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  li = list(map(int, input().strip()))

  idx = 0
  for i in range(len(li)-1, 0, -1):
    if li[i-1] >= li[i]:
      continue
    else:
      idx = li[i-1]
      backList = li[i-1:]
      fontList = li[:i-1]
      backList.sort()
      for j in range(len(backList)):
        if backList[j] > idx:
          fontList.append(backList.pop(j))
          fontList.extend(backList)
          break
    break
  if idx == 0:
    print('BIGGEST')
  else:
    print(''.join(map(str,fontList)))