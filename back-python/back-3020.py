# 답 봐야할듯 ;;
import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n, h = map(int, input().split())

top = []
bottom = []
for i in range(n):
  if i%2 ==0:
    bottom.append(int(input()))
  else:
    top.append(int(input()))

top.sort()
bottom.sort()
def binery_search(arr, target):
  start = 0
  end = len(arr)

  while start <end:
    mid = (start +end)//2
    
    if arr[mid] > target:
      end = mid
    elif arr[mid] <= target:
      start = mid+1
  return len(arr) - start

min_val = n
sol = 0
for i in range(1, h+1):
  s = binery_search(bottom, i - 1) + binery_search(top, h-i)
  if s < min_val:
    min_val = s
    sol = 1
  elif s == min_val:
    sol +=1

print(min_val, sol)
