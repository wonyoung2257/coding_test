import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

M = int(input())
N = int(input())

def prime_number(x):  
  if x == 1:
    return False
  for i in range(2, x):
    if x % i ==0:
      return False
  return True

answer = []

for i in range(M, N+1):  
  if prime_number(i):
    answer.append(i)

if len(answer) == 0:
  print(-1)
else:
  print(sum(answer))
  print(min(answer))