import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline
A, B, C= map(int, input().split(' '))

C-=B
if C <= 0:
  print(-1)
else:
  print(A//C +1)