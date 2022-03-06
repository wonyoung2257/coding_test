import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort(reverse=True)

for i in range(1, N+1):
  arr[i-1] *= i

print(max(arr))