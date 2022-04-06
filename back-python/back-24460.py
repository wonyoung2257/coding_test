# 포기!
import sys
sys.setrecursionlimit(10**8)
sys.stdin = open("input_py.txt", "r")

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

def sol(n, x, y):
  if n == 2:
    x -=1
    y -=1
    return sorted([table[x][y], table[x-1][y], table[x][y-1], table[x-1][y-1]])[1]

  return sorted([(sol(n//2, x- n//2, y- n//2)), (sol(n//2, x, y- n//2)),(sol(n//2, x- n//2, y)),(sol(n//2, x, y))])[1]

print(sol(n,n,n))