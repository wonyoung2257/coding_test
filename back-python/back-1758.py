import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

answer = 0
rank = 1
for i in arr:
  cul = i - (rank-1)
  rank+=1
  if cul >0:
    answer+=cul
print(answer)