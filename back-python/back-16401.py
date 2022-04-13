import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

m, n = map(int ,input().split())

snack = list(map(int, input().split()))

def fun(mid):
  temp = 0
  for i in snack:
    if i < mid:
      continue
    else:
      temp += i//mid
  return temp

def binery_search():
  start = 1
  end = max(snack)

  while start <= end:
    mid = (start+end)//2

    if fun(mid) >= m:
      start = mid+1
    else:
      end = mid-1
  
  return start-1

print(binery_search())