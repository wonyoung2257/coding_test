import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split(' ')))

def dinary_search(start, end):
  
  while start <= end:
    mid = (start+end) //2

    if mid == arr[mid]:
      return mid
    elif mid > arr[mid]:
      start = mid+1
    else:
      end = mid -1
  
  return None

num = dinary_search(0, len(arr)-1)
if num == None:
  print(-1)
else:
  print(num)