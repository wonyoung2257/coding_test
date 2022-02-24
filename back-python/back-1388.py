import sys
sys.stdin = open("input_py.txt", "r")

n, m = map(int, sys.stdin.readline().split())
li = [input() for _ in range(n)]

cnt = 0
for i in range(n):
  pre = 'o'
  for j in range(m):    
    if li[i][j] == '|':
      pre = '|'
      continue
    else:
      if pre !='-':
        cnt+=1
        pre = li[i][j]

for i in range(m):
  pre = 'o'
  for j in range(n):    
    if li[j][i] == '-':
      pre = '-'
      continue
    else:
      if pre !='|':
        cnt+=1
        pre = li[j][i]

print(cnt)