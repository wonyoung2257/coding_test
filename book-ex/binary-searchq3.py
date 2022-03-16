import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n, c = map(int, input().split(' '))

arr = [int(input())for _ in range(n)]
arr.sort()
start = 1
end = arr[-1] - arr[0]

result = 0
while start <= end:
  mid = (start + end) //2
  count = 1
  value = arr[0]

  # 공유기가 설치가 가능한상황 찾기
  for i in range(1, n):
    if arr[i] >= value + mid:
      count +=1
      value = arr[i]
  
  if count >= c:
    start = mid +1
    result = mid
  else:
    end = mid -1
  
print(result)