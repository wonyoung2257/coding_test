# 답봄
# 10^5 * 10^5 배열을 만들면 메모리 초과가 발생
import sys
sys.stdin = open("input_py.txt", "r")

n = int(input())
k = int(input())

start = 0
end = k

answer = 0
while start < end:
  mid = (start+end)//2
  
  temp = 0
  for i in range(1, n+1):
    temp += min(mid//i, n)
  
  if temp >= k:
    answer = mid
    end = mid
  else:
    start = mid +1

print(answer)