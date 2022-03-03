import sys

input = sys.stdin.readline

def fun(arr):
  i = 0
  while i+2 <len(arr):
    if arr[i] < arr[i+1] +arr[i+2]:
      return arr[i]+arr[i+1] +arr[i+2]
    i+=1
  return -1

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

print(fun(arr))