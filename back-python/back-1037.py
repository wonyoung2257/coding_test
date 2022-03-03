import sys

sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

T = int(input())
arr = list(map(int, input().split()))
arr.sort()
if T >1:
  print(arr[0]*arr[-1])
else:
  print(arr[0]**2)