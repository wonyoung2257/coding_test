import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
ruby = list(int(input()) for _ in range(m))

def fun(mid):
  temp  = 0
  for i in ruby:
    if i%mid == 0:
      temp += i//mid
    else:
      temp += i//mid
      temp +=1
  return temp

def dinery_search():
  start = 0
  end = max(ruby)
  while start <= end:
    mid = start + (end-start)//2

    if fun(mid) > n:
      start = mid+1
    else:
      end = mid -1
  
  return start

print(dinery_search())