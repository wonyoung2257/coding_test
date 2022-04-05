import sys
sys.setrecursionlimit(10**6)

def make_start(n):
  if n == 1:
    return ['*']
  
  starts = make_start(n//3)
  arr = []
  for s in starts:
    arr.append(s*3)
  for s in starts:
    arr.append(s + ' '*(n//3) +s)
  for s in starts:
    arr.append(s*3)
  
  return arr

n = int(input())

print('\n'.join(make_start(n)))