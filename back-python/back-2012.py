import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

rank = 1
answer = 0
for i in arr:
  cul = abs(i-rank)
  rank+=1
  answer+= cul
print(answer)