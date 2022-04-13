import sys
sys.stdin = open("input_py.txt", "r")

n, m = map(int ,input().split())
arr = sorted(list(map(int, input().split())))

start = max(arr)
end = sum(arr)
answer = 1e9
while start <= end:
  mid = (start + end)//2
  cnt = 1
  temp = 0
  for i in arr:
    if temp+i <=mid:
      temp +=i
    else:
      temp = i
      cnt +=1
    if cnt >m:
      break
      
  if cnt > m:
    start = mid +1
  else:
    if mid >= max(arr):
      answer = min(answer, mid)
    end = mid -1

print(answer)
