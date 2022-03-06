import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(' ')))

arr.sort()
if N == 1:
  print(arr[0])
else:
  if len(arr) % 2 == 0:
    temp = len(arr)//2 -1
  else :
    temp = len(arr)//2
  print(arr[temp])