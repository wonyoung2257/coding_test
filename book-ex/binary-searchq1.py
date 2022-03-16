import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N, x = map(int,input().strip().split(' '))
arr = list(map(int, input().split(' ')))

def min_index_search(start, end, target):
  min_idx = 1e9
  while start <= end:
    mid = (start + end) //2
    
    if arr[mid] == target:
      # 값을 찾았는데 같은 값이 앞쪽에 있을때
      if mid == 0:
        return mid
      if arr[mid-1] == arr[mid]:
        min_idx = min(min_idx, mid)
        end = mid -1
        continue
      else:
        return mid
    
    if arr[mid] > target:
      end = mid -1
    else:
      start = mid +1
  
  return -1

def max_index_search(start, end, target):
  max_idx = -1e9
  while start <= end:
    mid = (start + end) //2
    
    if arr[mid] == target:
      # 값을 찾았는데 같은 값이 앞쪽에 있을때
      if mid == len(arr):
        return mid
      if arr[mid+1] == arr[mid]:
        max_idx = max(max_idx, mid)
        start = mid+1
        continue
      else:
        return mid
    
    if arr[mid] > target:
      end = mid -1
    else:
      start = mid +1
  
  return -1

min_i = min_index_search(0, len(arr)-1, x)
max_i = max_index_search(0, len(arr)-1, x)
if min_i == -1:
  print(-1)
else:
  print(max_i - min_i +1)