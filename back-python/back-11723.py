import sys
sys.stdin = open("input_py.txt", "r")

M = int(input())
S = 0

for _ in range(M):
  li = list(sys.stdin.readline().strip().split())

  if len(li) == 1:
    if li[0] == 'all':
      S |= (1<<21) -1      
    elif li[0] == 'empty':
      S = 0
  else:
    num = int(li[1])
    if li[0] == 'add':
      S |= (1<<num)
    elif li[0] == 'remove':
      S &= ~(1<<num)

    elif li[0] == 'check':      
      if bin(S & (1<<num)) != bin(0):
        print(1)
      else: print(0)

    elif li[0] == 'toggle':
      S ^= (1<<num)
