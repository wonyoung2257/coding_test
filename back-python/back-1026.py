import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

A.sort()
B.sort(reverse=True)

total = 0
for i in range(N):
  total += A[i]*B[i]

print(total)