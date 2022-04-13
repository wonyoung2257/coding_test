# 최소 예산이 요청한 예산의 최소라는 보장이 없다.
import sys
sys.stdin = open("input_py.txt", "r")

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

start = 0
end = max(budget)
answer = 0
while start <= end:
  mid = (start+end)//2
  
  temp = 0
  for el in budget:
    if el <= mid:
      temp += el
    else:
      temp += mid

  if temp > m:
    end = mid -1
  else:
    start = mid +1

print(end)