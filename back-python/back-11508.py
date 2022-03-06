import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
total = 0
for i in range(len(arr)//3):
  total += arr.pop()
  total += arr.pop()
  arr.pop()

total += sum(arr)
print(total)
